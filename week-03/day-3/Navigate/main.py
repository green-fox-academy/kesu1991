from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/1900")
def the_legend_of_1900():
    return render_template("1900.html")

@app.route("/the_terminal")
def the_terminal():
    return render_template("the_terminal.html")

@app.route("/forrest_gump")
def forrest_gump():
    return render_template("forrest_gump.html")

@app.route("/the_post")
def the_post():
    return render_template("the_post.html")

@app.route("/avengers_endgame")
def avengers_endgame():
    return render_template("avengers_endgame.html")

@app.route("/")
def home():
    return render_template("list_movies.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


