import psycopg2
import pandas as pd
import sys

def employee_csv(file_path, table_name, dbname, host, user, pwd):

    # Connect to db
    conn = psycopg2.connect(dbname=dbname, host=host,\
        user=user, password=pwd)
    print("Connecting to Database")

    # Creat cursor
    cur = conn.cursor()
    f = open(file_path, "r")

    # Truncate the table first
    cur.execute("Truncate {} Cascade;".format(table_name))
    print("Truncated {}".format(table_name))

    # Load table from the file with header
    cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
    cur.execute("commit;")
    print("Loaded data into {}".format(table_name))

    # Close connection
    conn.close()
    print("DB connection closed.")


# Execution Example
file_path = 'employees.csv'
table_name = 'employee'
dbname = 'postgres'
host = 'localhost'
user = 'postgres'
pwd = 'SkBr2010421'

employee_csv(file_path, table_name, dbname, host, user, pwd)

"""
create table employee (
                    id INT,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    birth_date DATE,
                    gender VARCHAR(50),
                    monthly_salary INT);
"""

