import psycopg2, datetime, pandas as pd, json, sys, re
from pprint import pprint


def users(file_path, table_name, dbname, host, user, pwd, variable):

    # Connect to db
    conn = psycopg2.connect(dbname=dbname, host=host,\
    user=user, password=pwd)
    print("Connecting to Database")

    # Creat cursor
    cur = conn.cursor()

    # Parse json
    with open(file_path) as f:
        data = json.load(f)

    # Insertion
        unique_userid = set()

        for item in data:

            if variable in item.keys():
                unique_userid.add(item[variable])

        unique_userid = list(unique_userid)

    #print(item['user'])

        for item in unique_userid:
            
            result = []
            result = [item]

            postgres_insert_query = " INSERT INTO users (user_id) VALUES (%s)"

            cur.execute(postgres_insert_query, (result))
        

        conn.commit()
        cur.close()
 
# Execution Example


variable = "user"
file_path = 'history.json'
table_name = 'users'
dbname = 'slack'
host = 'localhost'
user = 'postgres'
pwd = '********'

users(file_path, table_name, dbname, host, user, pwd, variable)