import argparse
#import psycopg2
import csv
# Define database connection parameters
DB_NAME = "UniversalNetworkDataHub_Jamaica"
DB_USER = "gpuser"
DB_PASSWORD = "gpuser@123"
DB_HOST = "192.168.4.127"
DB_PORT = "5432"

def connect_to_database():
    """Connect to the PostgreSQL database."""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def execute_query(conn, query):
    """Execute SQL query and return results."""
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def write_to_csv(data, filename):
    """Write data to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['level', 'MO_Table', 'MO_Table_Column', 'MO_Table_Column_Golden_Value', 'Current_value'])
        writer.writerows(data)

def get_dependent_tables_and_columns(table, column):
    """Get dependent tables and columns for a given table and column."""
    dependencies = []
    for record in data:
        if record['Table'] == table and record['Column'] == column:
            for i in range(1, 4):
                condition_table_key = f'Condition_Table_{i}'
                condition_table_column_key = f'Condition_Table_{i}_Column'
                condition_table_value_key = f'Condition_Table_{i}_Column_Value'
                if condition_table_key in record and condition_table_column_key in record:
                    dependencies.append((record[condition_table_key], record[condition_table_column_key], record[condition_table_value_key]))
    return dependencies

def perform_gpl_audit(mo_table, mo_table_column, timestamp, site):
    """Perform Golden Value Audit."""
    conn = connect_to_database()
    gpl_audit_data = []

    for record in data:
        table = record['Table']
        column = record['Column']
        golden_value = record['Column_Golden_Value']
        join_column = record.get('Join_Column', None)
        
        if mo_table == "ALL" or mo_table == table:
            query = f'SELECT "dbo"."{table}"."{column}" FROM "dbo"."{table}"'
            if join_column:
                query += f' JOIN "dbo"."{join_column}" AS ct0 ON "dbo"."{table}"."DimensionId" = ct0."DimensionId"'
            if mo_table_column and mo_table_column != column:
                query += f' WHERE "{mo_table_column}" = \'{timestamp}\''
            if site:
                query += f' AND ct0."Market" = \'{site}\''
                
            rows = execute_query(conn, query)
            
            for row in rows:
                current_value = row[0]
                # Check if the current value matches the golden value
                if current_value != golden_value:
                    gpl_audit_data.append(('Level', table, column, golden_value, current_value))

            # Check for dependencies and recursively perform audit
            dependencies = get_dependent_tables_and_columns(table, column)
            for dependency in dependencies:
                dependent_table, dependent_column, dependency_value = dependency
                perform_gpl_audit(dependent_table, dependent_column, dependency_value, site)

    conn.close()
    return gpl_audit_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Golden Value Audit Script")
    parser.add_argument("MO_TABLE", nargs="?", default="ALL", help="Table to perform GPL Audit on (default: ALL)")
    parser.add_argument("--MO_Table_Column", help="Column of MO_TABLE to filter (default: None)")
    parser.add_argument("--TimeStamp", help="Timestamp to filter MO_Table_Column (default: None)")
    parser.add_argument("--Site", help="Site to filter (default: None)")
    args = parser.parse_args()

    # Data provided in the question
    data =[
       {
        "Table": "ER_L_ReportConfigEUtraBestCellAnr",
        "Column": "timeToTriggerA3",
        "Column_Golden_Value": "321"
    }]

    # Perform GPL Audit
    gpl_audit_data = perform_gpl_audit(args.MO_TABLE, args.MO_Table_Column, args.TimeStamp, args.Site)

    # Write audit results to CSV
    write_to_csv(gpl_audit_data, "gpl_audit_results.csv")
