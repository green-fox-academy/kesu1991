import psycopg2
import sys, re

con = psycopg2.connect(

    host='localhost',
    database='postgres',
    user='postgres',
    password='SkBr2010421'

)

# Create cursor
cursor = con.cursor()


###### Add a song 
if sys.argv[1] == 'a':

    # Query
    insert_query = 'INSERT INTO music (artist, title) VALUES (%s,%s)'
    select_query = 'SELECT * FROM music'

    # Regular Expression
    found_artist = re.search(r'"?([a-zA-Z *]+)"?.', sys.argv[2])
    found_title = re.search(r'(--title\s)?"?(.*)"+', sys.argv[3])

    # Cursor execute
    value_to_insert = (found_artist.group(1), found_title.group(2))
    cursor.execute(insert_query, value_to_insert)
    cursor.execute(select_query)


###### Listing available songs
if sys.argv[1] == 'l':

    # Regular Expression
    found_artist = re.search(r'(--artist\s)?"+(.*)"+', sys.argv[2])

    # Query    
    select_query = "SELECT artist, title FROM music WHERE artist LIKE %(String)s OR title LIKE %(String)s"
    
    # Cursor execute
    cursor.execute(select_query, {"String": "%"+found_artist.group(2)+"%"})


###### Delete a song
if sys.argv[1] == 'd':

    # Query
    delete_query = "DELETE FROM music WHERE id = %(Number)i"

    # Cursor execute
    cursor.execute(delete_query, {"Number": sys.argv[2]})

# Commit
con.commit()

# Print result
print(cursor.fetchall())

# Close everthing
cursor.close()
con.close()



