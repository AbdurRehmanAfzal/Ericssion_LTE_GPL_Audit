import psycopg2
import csv
import json
from datetime import datetime, timezone, timedelta


def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Function to establish database connection
def connect_to_db(Vandor):
    database = ""
    if Vandor == "Ericsson":
        database = "EricssonDataHub"
    elif Vandor == "Huawei":
        database = "HuaweiDataHub"
    else:
        print("Error: Invalid Vendor specified")
        return None, None

    try:
        connection = psycopg2.connect(user="parser",
                                      password="parser@123",
                                      host="192.168.15.51",
                                      port="5432",
                                      database=database)
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
        return None, None

# Function to execute SQL query and fetch results
def execute_query(cursor, query):
    try:
        cursor.execute(query)
        return cursor.fetchall(), None
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error_message = str(e)
        return [], error_message

def check_table_exists(cursor, table_name):
    query = f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}');"
    result, error = execute_query(cursor, query)
    if error:
        return False, error
    return result[0][0], None

def check_column_exists(cursor, table_name, column_name):
    query = f"SELECT EXISTS (SELECT FROM information_schema.columns WHERE table_name = '{table_name}' AND column_name = '{column_name}');"
    result, error = execute_query(cursor, query)
    if error:
        return False, error
    return result[0][0], None

def write_to_csv(results, vendor):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'debug_audit_results_{timestamp}.csv'
    filename = "/var/www/html/" + filename
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if vendor == "Huawei":
                writer.writerow(['Level', 'Market', 'Table', 'Column', 'Golden_Value', 'Current_Value'])
                for result in results:
                    level = f"{result[1]}:{result[2]}"  # Concatenate SiteID and Cell
                    writer.writerow([level, result[0], result[3], result[4], result[5], result[6]])
            else:
                writer.writerow(['Level', 'Market', 'SiteId', 'Table', 'Column', 'Golden_Value', 'Current_Value'])
                for result in results:
                    writer.writerow(result)
    except IOError as e:
        print(f"Error writing to CSV: {e}")
    return filename

def write_to_log(errors):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'query_errors_{timestamp}.log'
    try:
        with open(filename, mode='w') as file:
            for error in errors:
                file.write(f"Query: {error['query']} Error: {error['error_message']}\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")

def write_missing_to_log(missing_tables, missing_columns):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'missing_tables_columns_{timestamp}.log'
    try:
        with open(filename, mode='w') as file:
            if missing_tables:
                file.write("Missing Tables:\n")
                for table in missing_tables:
                    file.write(f"{table}\n")
            if missing_columns:
                file.write("\nMissing Columns:\n")
                for table, column in missing_columns:
                    file.write(f"Table: {table}, Column: {column}\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")


def convert_to_utc(timestamp_str):
    dt = datetime.fromisoformat(timestamp_str)
    dt = dt.replace(tzinfo=timezone.utc)
    return dt

def construct_query(table, entry, source_timestamp, vendor, OPCO, Market, Cluster):
    try:
        conditions = []
        join_clauses = []
        where_clauses = []

        # Collecting conditions from the entry
        if 'Join_Column' in entry:
            for i in range(1, 4):
                condition_table = entry.get(f"Condition_Table_{i}")
                condition_column = entry.get(f"Condition_Table_{i}_Column")
                condition_value = entry.get(f"Condition_Table_{i}_Column_Value")
                operator = entry.get(f"operator_{i}")
                if condition_table and condition_column and condition_value and operator:
                    conditions.append((condition_table, condition_column, condition_value, operator))

        if vendor == "Huawei":
            query = f'''
            SELECT "dbo"."{table}"."Level", "dbo"."Dimensions"."Market", "dbo"."Dimensions"."SiteID", "dbo"."Dimensions"."Cell", "dbo"."{table}"."{entry['Column']}"
            FROM "dbo"."{table}"
            JOIN "dbo"."Dimensions" ON "dbo"."{table}"."DimensionId" = "dbo"."Dimensions"."DimensionId"
            '''
        else:
            query = f'''
            SELECT "dbo"."{table}"."Level", "dbo"."Dimensions"."Market", "dbo"."Dimensions"."SiteID", "dbo"."{table}"."{entry['Column']}"
            FROM "dbo"."{table}"
            JOIN "dbo"."Dimensions" ON "dbo"."{table}"."DimensionId" = "dbo"."Dimensions"."DimensionId"
            '''

        # Handling timestamp filter
        if source_timestamp:
            midnight_today = datetime.combine(source_timestamp.date(), datetime.min.time())
            midnight_tomorrow = midnight_today + timedelta(days=1)
            midnight_today_str = midnight_today.isoformat() + "+00:00"
            midnight_tomorrow_str = midnight_tomorrow.isoformat() + "+00:00"
            where_clauses.append(f'"dbo"."{table}"."DateTime" >= \'{midnight_today_str}\' and "dbo"."{table}"."DateTime" < \'{midnight_tomorrow_str}\'')

        if OPCO:
            where_clauses.append(f'"dbo"."Dimensions"."OPCO" = \'{OPCO}\'')
        if Market:
            market_conditions = ','.join([f'\'{m}\'' for m in Market])
            where_clauses.append(f'"dbo"."Dimensions"."Market" in ({market_conditions})')
        if Cluster:
            cluster_conditions = ','.join([f'\'{c}\'' for c in Cluster])
            where_clauses.append(f'"dbo"."Dimensions"."Cluster" in ({cluster_conditions})')

        # Handling conditions
        for i, (condition_table, condition_column, condition_value, operator) in enumerate(conditions):
            if condition_table == table:
                where_clauses.append(f'"dbo"."{condition_table}"."{condition_column}" {operator} \'{condition_value}\'')
            else:
                join_clauses.append(f'JOIN "dbo"."{condition_table}" AS ct{i} ON "dbo"."{table}"."DimensionId" = ct{i}."DimensionId"')
                where_clauses.append(f'ct{i}."{condition_column}" {operator} \'{condition_value}\'')

        query += ' '.join(join_clauses)
        if where_clauses:
            query += ' WHERE ' + ' AND '.join(where_clauses)
        return query
    except KeyError as e:
        print(f"KeyError: {e}")
        return None

def main(Vandor, Technology, MO=[], Parameter=[], SourceTimestamp=None, OPCO=None, Market=None, Cluster=None):
    if SourceTimestamp:
        SourceTimestamp = convert_to_utc(SourceTimestamp)
    if Vandor == "Ericsson":
        if Technology == "LTE":
            data = load_data('ericsson_lte_data.json')
        elif Technology == "WCDMA":
            data = load_data('ericsson_wcdma_data.json')
        elif Technology == "All":
            data = load_data('ericsson_lte_data.json') + load_data('ericsson_wcdma_data.json')
        else:
            print("Error: Invalid Technology specified for Ericsson")
            return
    elif Vandor == "Huawei":
        if Technology == "LTE":
            data = load_data('huawei_lte_data.json')
        elif Technology == "WCDMA":
            data = load_data('huawei_wcdma_data.json')
        elif Technology == "All":
            data = load_data('huawei_lte_data.json') + load_data('huawei_wcdma_data.json')
        else:
            print("Error: Invalid Technology specified for Huawei")
            return
    else:
        print("Error: Invalid Vendor specified")
        return

    tables = set(MO) if MO else {entry["Table"] for entry in data}
    columns = set(Parameter) if Parameter and Parameter != 'All' else None

    connection, cursor = connect_to_db(Vandor)
    if connection is None or cursor is None:
        return

    audit_results = []
    query_errors = []
    missing_tables = []
    missing_columns = []

    for table in tables:
        table_exists, error = check_table_exists(cursor, table)
        if error:
            query_errors.append({"query": f"Check table {table}", "error_message": error})
            continue
        if not table_exists:
            missing_tables.append(table)
            continue

        table_entries = [entry for entry in data if entry["Table"] == table]
        if columns is not None:
            table_entries = [entry for entry in table_entries if entry["Column"] in columns]

        for entry in table_entries:
            column_exists, error = check_column_exists(cursor, table, entry["Column"])
            if error:
                query_errors.append(
                    {"query": f"Check column {entry['Column']} in table {table}", "error_message": error})
                continue
            if not column_exists:
                missing_columns.append((table, entry["Column"]))
                continue

            query = construct_query(table, entry, SourceTimestamp, Vandor, OPCO, Market, Cluster)
            if query is not None:
                results, error_message = execute_query(cursor, query)
                if error_message:
                    query_errors.append({"query": query, "error_message": error_message})
                if results:
                    for result in results:
                        if Vandor == "Huawei":
                            level = f"{result[2]}:{result[3]}"
                            siteId = result[2]
                            current_value = result[4]
                            market = result[1]
                        else:
                            level = result[0]
                            market = result[1]
                            siteId = result[2]
                            current_value = result[3]
                        gVal = entry.get("Column_Golden_Value")
                        if gVal is None:
                            gVal = entry.get("Golden Value")
                        golden_value = str(gVal).lower()
                        current_value_str = str(current_value).lower()

                        if not (
                                (golden_value == "1" and current_value_str == "true") or
                                (golden_value == "0" and current_value_str == "false") or
                                (golden_value == "true" and current_value_str == "true") or
                                (golden_value == "TRUE" and current_value_str == "1") or
                                (golden_value == "1" and current_value_str == "TRUE") or
                                (golden_value == "True" and current_value_str == "1") or
                                (golden_value == "1" and current_value_str == "True") or
                                (golden_value == "false" and current_value_str == "false") or
                                (golden_value == "0" and current_value_str == "off") or
                                (golden_value == "1" and current_value_str == "ACTIVATED") or
                                (golden_value == current_value_str) or
                                (golden_value in [val.strip() for val in current_value_str.replace('[', '').replace(']', '').replace('"', '').split('-')])
                        ):
                            if Vandor == "Huawei":
                                audit_results.append([result[1], result[2], result[3], table, entry["Column"], gVal, current_value])
                            else:
                                audit_results.append([level, market, siteId, table, entry["Column"], gVal, current_value])
                else:
                    print(f"No data found for table '{table}'")

    audit_results = list(map(list, set(map(tuple, audit_results))))

    file = write_to_csv(audit_results, Vandor)

    if query_errors:
        write_to_log(query_errors)

    if missing_tables or missing_columns:
        write_missing_to_log(missing_tables, missing_columns)

    if connection is not None:
        cursor.close()
        connection.close()
    return file