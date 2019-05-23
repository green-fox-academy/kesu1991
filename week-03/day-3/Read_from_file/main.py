from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/1900")
def the_legend_of_1900():
	text = open('1900.txt', 'r+')
	content = text.read()
	text.close()
	return render_template('movie.html', text = content)

@app.route("/avengers_endgame")
def avengers_endgame():
	text = open('avengers_endgame.txt', 'r+')
	content = text.read()
	text.close()
	return render_template('movie.html', txt = content)

@app.route("/forrest_gump")
def forrest_gump():
	text = open('forrest_gump.txt', 'r+')
	content = text.read()
	text.close()
	return render_template('movie.html', ftxt = content)

@app.route("/the_post")
def the_post():
	text = open('the_post.txt', 'r+')
	content = text.read()
	text.close()
	return render_template('movie.html', ptxt = content)

@app.route("/the_terminal")
def the_terminal():
	text = open('the_terminal.txt', 'r+')
	content = text.read()
	text.close()
	return render_template('movie.html', ttxt = content)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


