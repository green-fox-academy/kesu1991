import psycopg2, datetime, pandas as pd, json, sys, re
from pprint import pprint

# Connect to db
conn = psycopg2.connect(dbname="slack", host="localhost",\
user="postgres", password="********")
print("Connecting to Database")

# Creat cursor
cur = conn.cursor()

# Parse json
with open('history.json') as f:
    data = json.load(f)

# Insertion
count = 0
for item in data:

    if 'user' in item.keys() and 'client_msg_id' in item.keys() and 'reactions' in item.keys():

        result = []

        user_id_reac = item['user']
        mesg_id_reac = item['client_msg_id']
        
        # Reaction part
        for item_reac in item['reactions']:
            
            count += 1
            
            result_reac = []

            emoji = item_reac['name']

            result_reac = [count, user_id_reac, mesg_id_reac, emoji]

            postgres_insert_query_reac = "INSERT INTO reaction (id, user_id, message_id, reaction) VALUES (%s,%s,%s,%s)"

            c = cur.execute(postgres_insert_query_reac, (result_reac))


conn.commit()
cur.close()

