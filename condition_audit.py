import psycopg2
import csv
import argparse
import ast
import json


# Hardcoded data list
data = [
    {
        "Table": "L_AdmissionControl",
        "Column": "dlTransNwBandwidth",
        "Column_Golden_Value": 1000,
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "NOT (BTC)"
    },
    {
        "Table": "L_AdmissionControl",
        "Column": "ulTransNwBandwidth",
        "Column_Golden_Value": 1000,
        "Join_Column": "DimensionId",
        "Condition_Table_1": "Dimensions",
        "Condition_Table_1_Column": "Market",
        "Condition_Table_1_Column_Value": "NOT (BTC)"
    },
    {
        "Table": "L_QciProfilePredefined",
        "Column": "qciSubscriptionQuanta",
        "Column_Golden_Value": 500,
        "Join_Column": "DimensionId",
        "Condition_Table_1": "L_QciProfilePredefined",
        "Condition_Table_1_Column": "qciProfilePredefinedId",
        "Condition_Table_1_Column_Value": "qciProfilePredefinedId != qci1 & qci5 & qci6 & qci7 & qci8 & qci9"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "crsGain",
        "Column_Golden_Value": 0,
        "Join_Column": "DimensionId",
        "Condition_Table_1": "KPIs_Cell_Weekly_4G",
        "Condition_Table_1_Column": "DL PRB Usage",
        "Condition_Table_1_Column_Value": "DL PRB USAGE > 40%"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "crsGain",
        "Column_Golden_Value": -100,
        "Join_Column": "DimensionId",
        "Condition_Table_1": "KPIs_Cell_Weekly_4G",
        "Condition_Table_1_Column": "DL PRB Usage",
        "Condition_Table_1_Column_Value": "30% < DL PRB USAGE <= 40%"
    },
    {
        "Table": "L_EUtranCellFDD",
        "Column": "crsGain",
        "Column_Golden_Value": -300,
        "Join_Column": "DimensionId",
        "Condition_Table_1": "KPIs_Cell_Weekly_4G",
        "Condition_Table_1_Column": "DL PRB Usage",
        "Condition_Table_1_Column_Value": "DL PRB USAGE <= 30%"
    },
    {
        "Table": "L_AnrFunctionEUtran",
        "Column": "anrInterFreqState",
        "Column_Golden_Value": "ACTIVATED",
        "Join_Column": "DimensionId",
        "Condition_Table_1": "EUtranCellFDD",
        "Condition_Table_1_Column": "dl256QamEnabled",
        "Condition_Table_1_Column_Value": "dl256QamEnabled > 1"
    }
]

# Function to establish database connection
def connect_to_db():
    try:
        connection = psycopg2.connect(user="gpuser",
                                      password="gpuser@123",
                                      host="192.168.4.127",
                                      port="5432",
                                      database="UniversalNetworkDataHub_Jamaica")
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
        return None, None

# Function to execute SQL query and fetch results
def execute_query(cursor, query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Error: {e}")
        cursor.connection.rollback()  # Rollback the transaction to clear the error
        return []

# Function to write results to CSV file
def write_to_csv(results):
    try:
        with open('audit_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Level', 'Table', 'Column', 'Golden_Value', 'Current_Value'])
            writer.writerows(results)
    except IOError as e:
        print(f"Error writing to CSV: {e}")

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

        query = f'SELECT "{table}"."{entry["Column"]}" FROM "{table}"'
        
        # if entry["Table"] == "L_QciProfilePredefined":
        #     if entry["Column"] == "rlfProfileRef":
        #         query = f'SELECT SUBSTRING("{table}"."{entry["Column"]}" FROM \'RlfProfile=[0-9]+\' FOR \'RlfProfile=0\') AS "rlfProfileRef" FROM "{table}"'
        #     else:
        #         query = f'SELECT "{table}"."{entry["Column"]}" FROM "{table}"'
        if entry["Table"] == "L_QciProfilePredefined" and entry["Column"] == "drxProfileRef":
            query = f'SELECT SUBSTRING("{table}"."{entry["Column"]}" FROM \'DrxProfile=[0-9]+\') AS "drxProfileRef" FROM "{table}"'
        # elif entry["Table"] == "L_QciProfilePredefined" and entry["Column"] == "rlfProfileRef":
        #     query = f'SELECT SUBSTRING("{table}"."{entry["Column"]}" FROM \'DrxProfile=[0-9]+\') AS "drxProfileRef" FROM "{table}"'
        # elif entry["Table"] == "L_QciProfilePredefined" and entry["Column"] == "logicalChannelGroupRef":
        #     query = f'SELECT SUBSTRING("{table}"."{entry["Column"]}" FROM \'vsDataQciTable=default,vsDataLogicalChannelGroup=[0-9]+\' FOR \'vsDataQciTable=default,vsDataLogicalChannelGroup=1\') AS "logicalChannelGroupRef" FROM "{table}"'
        else:
            query = f'SELECT "{table}"."{entry["Column"]}" FROM "{table}"'
        

        if conditions:
            for i, (condition_table, condition_column, condition_value, condition_type) in enumerate(conditions):
                if condition_type == "RANGE":
                    query += f'''
                    JOIN "{condition_table}" AS ct{i} ON "{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND {condition_column} {condition_value}
                    '''
                elif condition_type == "NOT":
                    query += f'''
                    JOIN "{condition_table}" AS ct{i} ON "{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND ct{i}."{condition_column}" != '{condition_value}'
                    '''
                elif condition_type == "NOT IN":
                    query += f'''
                    JOIN "{condition_table}" AS ct{i} ON "{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND ct{i}."{condition_column}" NOT IN ({', '.join([f"'{val.strip()}'" for val in condition_value])})
                    '''
                else:
                    query += f'''
                    JOIN "{condition_table}" AS ct{i} ON "{table}"."{entry["Join_Column"]}" = ct{i}."DimensionId" AND ct{i}."{condition_column}" = '{condition_value}'
                    '''

        if timestamp:
            if "WHERE" in query:
                query += f' AND "{table}"."timestamp" = \'{timestamp}\''
            else:
                query += f' WHERE "{table}"."timestamp" = \'{timestamp}\''

        if sites:
            site_conditions = " OR ".join([f'"{table}"."site" = \'{site}\'' for site in sites])
            if "WHERE" in query:
                query += f' AND ({site_conditions})'
            else:
                query += f' WHERE {site_conditions}'
                
        if entry["Table"] == "L_QciProfilePredefined" and entry["Column"] == "drxProfileRef":
            if "WHERE" in query:
                query += f' AND "{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''
            else:
                query += f' WHERE "{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''

            query += f'''
            JOIN "Dimensions" AS dim ON "{table}"."{entry["Join_Column"]}" = dim."DimensionId" AND dim."Market" = '{entry["Condition_Table_2_Column_Value"]}'
            '''
        # if entry["Table"] == "L_QciProfilePredefined" and entry["Column"] == "rlfProfileRef":
        #     if "WHERE" in query:
        #         query += f' AND "{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''
        #     else:
        #         query += f' WHERE "{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''

        #     query += f'''
        #     JOIN "Dimensions" AS dim ON "{table}"."{entry["Join_Column"]}" = dim."DimensionId" AND dim."Market" = '{entry["Condition_Table_2_Column_Value"]}'
        #     '''
        # if entry["Table"] == "L_QciProfilePredefined" and entry["Column"] == "logicalChannelGroupRef":
        #     if "WHERE" in query:
        #         query += f' AND "{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''
        #     else:
        #         query += f' WHERE "{table}"."qciProfilePredefinedId" = \'{entry["Condition_Table_1_Column_Value"]}\''
        # return query
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

    # Connect to the database
    connection, cursor = connect_to_db()
    if connection is None or cursor is None:
        return

    all_tables = {entry["Table"] for entry in data} if tables == ["all"] else set(tables)

    # Iterate over each table and column
    for table in all_tables:
        for entry in data:
            if entry["Table"] == table or table == "all":
                query = construct_query(table, entry, timestamp, sites)
                if query is not None:
                    results = execute_query(cursor, query)
                    if results:
                        for result in results:
                            current_value = result[0]
                            if entry["Column_Golden_Value"] != current_value:
                                print(f"Audit finding: Table - {table}, Column - {entry['Column']}, "
                                      f"Golden Value - {entry['Column_Golden_Value']}, Current Value - {current_value}")
                    else:
                        print(f"No data found for table '{table}'")

    # Close the database connection
    if connection is not None:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()