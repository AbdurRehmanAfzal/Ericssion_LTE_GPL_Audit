import psycopg2
import csv
import argparse
import json
import os
data = [
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "dlTransNwBandwidth",
        "Column_Golden_Value": "1000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "NOT (BTC)"
    },
    {
        "Table": "ER_L_AdmissionControl",
        "Column": "ulTransNwBandwidth",
        "Column_Golden_Value": "1000",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "NOT (BTC)"
    },
    {
        "Table": "ER_L_AnrFunctionEUtran",
        "Column": "anrInterFreqState",
        "Column_Golden_Value": "ACTIVATED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "EUtranCellFDD",
        "Condition_Table_1_Column": "dl256QamEnabled",
        "Condition_Table_1_Column_Value": "> 1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "drxProfileRef",
        "Column_Golden_Value": "DrxProfile=1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1",
        "Condition_Table_2": "Dimensions",
        "Condition_Table_2_Column": "Market",
        "Condition_Table_2_Column_Value": "Panama"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "logicalChannelGroupRef",
        "Column_Golden_Value": "QciTable=default,LogicalChannelGroup=1",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "default"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": "500",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qciProfilePredefinedId != qci1 & qci5 & qci6 & qci7 & qci8 & qci9"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "crsGain",
        "Column_Golden_Value": "0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "KPIs_Cell_Weekly_4G",
        "Condition_Table_1_Column": "DL PRB Usage",
        "Condition_Table_1_Column_Value": "DL PRB USAGE > 40"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "crsGain",
        "Column_Golden_Value": "-100",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "KPIs_Cell_Weekly_4G",
        "Condition_Table_1_Column": "DL PRB Usage",
        "Condition_Table_1_Column_Value": "30 < DL PRB USAGE <= 40"
    },
    {
        "Table": "ER_L_EUtranCellFDD",
        "Column": "crsGain",
        "Column_Golden_Value": "-300",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "KPIs_Cell_Weekly_4G",
        "Condition_Table_1_Column": "DL PRB Usage",
        "Condition_Table_1_Column_Value": "DL PRB USAGE <= 30"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "default"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci1"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci2"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci3"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci4"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci5"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci6"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci7"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci8"
    },
    {
        "Table": "ER_L_QciProfilePredefined",
        "Column": "rlfProfileRef",
        "Column_Golden_Value": "RlfProfile=0",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "ER_L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qci9"
    }
]
# Function to establish database connection
def connect_to_db():
    try:
        connection = psycopg2.connect(user="gpuser",
                                      password="gpuser@123",
                                      host="192.168.4.127",
                                      port="5432",
                                      database="UniversalNetworkDataHubEH_Jamaica")
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
        cursor.connection.rollback()  # Rollback the transaction to clear the error
        error_message = str(e)
        return [], error_message

# Function to write results to CSV file
def write_to_csv(results):
    try:
        with open('conditional_debug_audit_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Level', 'Table', 'Column', 'Golden_Value', 'Current_Value'])
            writer.writerows(results)
    except IOError as e:
        print(f"Error writing to CSV: {e}")

# Function to write errors to a log file
def write_to_log(errors):
    try:
        with open('conditional_query_errors.log', mode='w') as file:
            for error in errors:
                file.write(f"Query: {error['query']}Error: {error['error_message']}")
    except IOError as e:
        print(f"Error writing to log file: {e}")

# Function to construct SQL query based on conditions
def construct_query(table, entry, timestamp, sites):
    try:
        conditions = []
        if 'Join_Column' in entry:
            for i in range(1, 4):
                condition_table = entry.get(f"Condition_Table_{i}")
                condition_column = entry.get(f"Condition_Table_{i}_Column")
                condition_value = entry.get(f"Condition_Table_{i}_Column_Value")
                if condition_table and condition_column and condition_value:
                    if ">" in condition_value or "<" in condition_value or "=" in condition_value:
                        conditions.append((condition_table, condition_column, condition_value, "RANGE"))
                    elif "NOT" in condition_value:
                        condition_value = condition_value.replace("NOT (", "").replace(")", "")
                        conditions.append((condition_table, condition_column, condition_value, "NOT"))
                    elif "!=" in condition_value:
                        condition_values = condition_value.split("!=")[1].split("&")
                        conditions.append((condition_table, condition_column, condition_values, "NOT IN"))
                    else:
                        conditions.append((condition_table, condition_column, condition_value, "EQUALS"))

        query = f'SELECT "dbo"."{table}"."Level", "dbo"."{table}"."{entry["Column"]}" FROM "dbo"."{table}"'
        
        if entry["Table"] == "ER_L_QciProfilePredefined" and entry["Column"] == "drxProfileRef":
            query = f'SELECT SUBSTRING("dbo"."{table}"."{entry["Column"]}" FROM \'DrxProfile=[0-9]+\') AS "drxProfileRef" FROM  "dbo"."{table}"'
        elif entry["Table"] == "ER_L_QciProfilePredefined" and entry["Column"] == "rlfProfileRef":
            query = f'SELECT SUBSTRING("dbo"."{table}"."{entry["Column"]}" FROM \'RlfProfile=[0-9]+\') AS "rlfProfileRef" FROM "dbo"."{table}"'
        elif entry["Table"] == "ER_L_QciProfilePredefined" and entry["Column"] == "logicalChannelGroupRef":
            query = f'SELECT SUBSTRING("dbo"."{table}"."{entry["Column"]}" FROM \'vsDataQciTable=default,vsDataLogicalChannelGroup=[0-9]+\') AS "logicalChannelGroupRef" FROM "dbo"."{table}"'
        else:
            query = f'SELECT "dbo"."{table}"."Level", "dbo"."{table}"."{entry["Column"]}" FROM "dbo"."{table}"'
        
        if conditions:
            for i, (condition_table, condition_column, condition_value, condition_type) in enumerate(conditions):
                if condition_type == "RANGE":
                    query += f'''
                    JOIN "dbo"."{condition_table}" AS ct{i} ON "dbo"."{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND "ct{i}"."{condition_column}" {condition_value}
                    '''
                elif condition_type == "NOT":
                    query += f'''
                    JOIN "dbo"."{condition_table}" AS ct{i} ON "dbo"."{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND "ct{i}"."{condition_column}" != '{condition_value}'
                    '''
                elif condition_type == "NOT IN":
                    query += f'''
                    JOIN "dbo"."{condition_table}" AS ct{i} ON "dbo"."{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND "ct{i}"."{condition_column}" NOT IN ({', '.join([f"'{val.strip()}'" for val in condition_value])})
                    '''
                else:
                    query += f'''
                    JOIN "dbo"."{condition_table}" AS ct{i} ON "dbo"."{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND "ct{i}"."{condition_column}" = '{condition_value}'
                    '''
        
        if entry["Table"] == "ER_L_QciProfilePredefined" and entry["Column"] == "drxProfileRef":
            query += f' WHERE "dbo"."{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''
            query += f'''
            JOIN "dbo"."Dimensions" AS dim ON "dbo"."{table}"."{entry["Join_Column"]}" = dim."DimensionId" AND dim."Market" = '{entry["Condition_Table_2_Column_Value"]}'
            '''
        if entry["Table"] == "ER_L_QciProfilePredefined" and entry["Column"] == "rlfProfileRef":
            query += f' WHERE "dbo"."{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''
            query += f'''
            JOIN "dbo"."Dimensions" AS dim ON "dbo"."{table}"."{entry["Join_Column"]}" = dim."DimensionId"
            '''
        if entry["Table"] == "ER_L_QciProfilePredefined" and entry["Column"] == "logicalChannelGroupRef":
            query += f' WHERE "dbo"."{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''
                
        return query
       
    except KeyError as e:
        print(f"KeyError: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Database Golden Value Audit Script')
    parser.add_argument('--tables', type=str, default='["all"]', help='List of tables in the form ["table1", "table2", ...] or ["all"]')
    parser.add_argument('--columns', type=str, default='["all"]', help='List of columns in the form ["column1", "column2", ...] or ["all"]')
    parser.add_argument('--timestamp', type=str, default=None, help='Timestamp value')
    parser.add_argument('--site', type=str, default='["all"]', help='List of sites in the form ["site1", "site2", ...] or ["all"]')
    args = parser.parse_args()

    tables = json.loads(args.tables)
    columns = json.loads(args.columns)
    sites = json.loads(args.site)
    timestamp = args.timestamp

    # Validate input
    if tables == ["all"] and (columns != ["all"] or timestamp is not None or sites != ["all"]):
        print("Error: If --tables is 'all', other options must also be 'all'")
        return

    if columns != ["all"] and not all(isinstance(column, str) for column in columns):
        print("Error: --columns argument must be a list of strings")
        return

    if sites != ["all"] and not all(isinstance(site, str) for site in sites):
        print("Error: --site argument must be a list of strings")
        return

    connection, cursor = connect_to_db()
    if not connection or not cursor:
        print("Failed to connect to the database.")
        return

    results = []
    errors = []

    for entry in data:
        if tables != ["all"] and entry["Table"] not in tables:
            continue

        if columns != ["all"] and entry["Column"] not in columns:
            continue

        query = construct_query(entry["Table"], entry, timestamp, sites)
        if query is None:
            continue

        print(f"Executing query: {query}")
        query_result, error_message = execute_query(cursor, query)
        if error_message:
            errors.append({'query': query, 'error_message': error_message})
            continue

        for result in query_result:
            if len(result) < 2:
                errors.append({'query': query, 'error_message': "Unexpected result format"})
                continue

            level, current_value = result
            golden_value = entry["Column_Golden_Value"]

            if current_value != golden_value:
                results.append([level, entry["Table"], entry["Column"], golden_value, current_value])

    write_to_csv(results)
    write_to_log(errors)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()