import random
from flask import (Flask, jsonify, request, redirect, url_for, render_template)
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "Type dir to see my exercise solutions! :)"

@app.route("/random_lan")
def random_lan():
    greet_list = ["Hello, John", "Nighao, yhgf!", "Ysha,adashi!"]
    greet_item = random.choice(greet_list)
    return render_template("random_lan.html", greet = greet_item)

@app.route("/random_lan2")
def random_lan2():

    greet_list = ["Hello", "Nihao", "Ysha"]
    name_list = ["John","Gary","Maria"]
    greet_item = random.choice(greet_list)
    name_item = random.choice(name_list)
    greet2 = greet_item + ", "+ name_item + "!"
    return render_template("random_lan2.html", greet = greet2)

@app.route("/products")
def products():

    products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)
    ]

    return render_template("products.html", greet = products)

@app.route("/articles")
def articles():

    articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
    ]

    return render_template("article.html", greet = articles)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


