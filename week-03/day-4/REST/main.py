from flask import (Flask, jsonify, request, redirect, url_for, render_template)
from movies import MovieCollection

app = Flask(__name__)
movie_collection = MovieCollection("movie.json")


@app.route("/")
def home():
    """Return a list of movies."""
    return "Welcome to my movies!"

@app.route('/api/movies/<choose>', methods=['GET'])
def retrieve_single(choose):

    if request.method == 'GET':
        return jsonify(movie_collection.read_movie(choose))


@app.route('/api/movies', methods=['GET'])
def retrieve_all():

    if request.method == 'GET':
        return jsonify(movie_collection.list_movie())

@app.route('/api/movies', methods=['POST'])
def add_movie(data):
        
    if request.method == 'POST':
        return jsonify(movie_collection.add_movie(data),key=request.headers['x-api-key'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


