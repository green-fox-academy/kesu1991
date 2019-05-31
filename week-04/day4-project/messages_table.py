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
for item in data:

    if 'user' in item.keys() and 'client_msg_id' in item.keys():

        result = []

        id_mesg = item['client_msg_id']
        user_mesg = item['user']
        message_mesg = item['text']
        sent_mesg = item['ts']

        found_time = re.search(r'([0-9]+).', sent_mesg)
        readable_ts = datetime.datetime.fromtimestamp(int(found_time.group(1))).isoformat()

        result = [id_mesg, user_mesg, message_mesg, readable_ts]

        postgres_insert_query = "INSERT INTO messages (id,user_id, message, sent_at) VALUES (%s,%s,%s,%s)"

        cur.execute(postgres_insert_query, (result))