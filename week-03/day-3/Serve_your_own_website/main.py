from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("firstwebsite.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


