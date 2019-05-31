import psycopg2
import sys, re

from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user_most_emojis/improve_it")
def impoved():

    # Connect to db slack
    con = psycopg2.connect(
        host='localhost',
        database='slack',
        user='postgres',
        password='SkBr2010421'
    )

    # Create cursor
    cursor = con.cursor()

    # Who got the most emojis?
    select_query = "SELECT user_id, count(reaction) FROM reaction GROUP BY user_id ORDER BY count(reaction) DESC LIMIT 5"

    # Cursor execute
    cursor.execute(select_query)
    table = cursor.fetchall()

    # Return result
    return render_template("test1.html", greet = table)
    cursor.close()
    con.close()


@app.route("/user_most_emojis")
def before_impoved():

    # Connect to db slack
    con = psycopg2.connect(
        host='localhost',
        database='slack',
        user='postgres',
        password='SkBr2010421'
    )

    # Create cursor
    cursor = con.cursor()

    # Who got the most emojis?
    select_query = "SELECT user_id, count(reaction) FROM reaction GROUP BY user_id ORDER BY count(reaction) DESC LIMIT 5"

    # Cursor execute
    cursor.execute(select_query)
    table = cursor.fetchall()

    # Return result
    return render_template("products.html", greet = table) 
    cursor.close()
    con.close()


@app.route("/user_no_comment")
def no_comment_user():
    # What is the percantage of the users have never written comments?
    return render_template("pie_chart.html")


@app.route("/emojis_rank")
def emojis_rank():
    # Top ten popular emojis.

    # Connect to db slack
    con = psycopg2.connect(
        host='localhost',
        database='slack',
        user='postgres',
        password='SkBr2010421'
    )

    # Create cursor
    cursor = con.cursor()

    # Who got the most emojis?
    most_emoji_query =  "SELECT reaction, count(reaction) FROM reaction GROUP BY reaction ORDER BY count(reaction) DESC LIMIT 10"
    
    # Cursor execute
    cursor.execute(most_emoji_query)
    most_emoji_list = cursor.fetchall()
    
    # main work
    percent_list = []
    for item in most_emoji_list:
        value = int((int(item[1]) / 1118 * 100))
        list_refer = (item[0],value)
        percent_list.append(list_refer)
        

    # Return result
    return render_template("his.html", greet = percent_list)
    cursor.close()
    con.close()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
