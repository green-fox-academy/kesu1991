###### Find oldest movie

import csv

with open('movie.csv') as csvfile:   
    readCSV = csv.reader(csvfile, delimiter=";")    
    titles = []
    years = []
    directors = []
    
    for row in readCSV:
        title = row[0]
        year = row[1]
        director = row[2]
        
        titles.append(title)
        years.append(year)
        directors.append(director)
        
    print(titles[years.index(min(years))])
	

###### Remove useless data
import pandas as pd
import numpy as np

full_data = pd.read_csv("election.csv",header=None)
missing_data = df[full_data.isnull().any(axis=1)]

nomissing_data = full_data.dropna()

print(nomissing_data)
print(missing_data)


###### Find the post with most popular comments
import json

# Read posts.json and create a object for it
with open('posts.json','rb') as json_file:  
    data = json_file.read()

obj = json.loads(data)

total_length = len(obj)  # Length of the object

d = {}    # Store the number of comments
not_none = []  # Store the position which comments does exists

for i in range(total_length):
    
    if obj[i]['comments'] is not None:
        not_none.append(i)
        d["comment_len_{0}".format(i)] = len(obj[i]['comments'])

num_of_comments = []        
num_of_comments = list(d.values())


sum_of_comments = []

for i in range(len(not_none)):
    refer = 0
    for j in range(num_of_comments[i]):
        refer = obj[not_none[i]]['comments'][j]['like_count'] + refer
        
    sum_of_comments.append(refer)

position = sum_of_comments.index(max(sum_of_comments))

print(f"Author with author id {obj[not_none[position]]['author_id']} get most popular comments.")

"""
Output : 

Author with author id 210 get most popular comments.
"""


###### USD transactions
import xml.etree.ElementTree as ET

tree = ET.parse('transactions.xml')
root = tree.getroot()

amount_USD = []
for amount in root.iter('amount'):
    if amount.attrib['currency'] == "USD":
        amount_USD.append(amount.text)
        
for i in range(len(amount_USD)):
    print(f"${amount_USD[i]}")
	
"""
Output : 

$2350
$8000
"""

###### 