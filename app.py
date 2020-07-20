from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_cors import CORS, cross_origin
# from flask_heroku import Heroku
# from environs import Env

import os

app = Flask(__name__)
CORS(app)
# heroku = Heroku(app)

# env = Env()
# env.read_env()
# DATABASE_URL = env("DATABASE_URL")

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
# Suppress python warning message
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(64))
    rating = db.Column(db.String(6))
    starrating = db.Column(db.Integer())


    def __init__(self, title, description, rating, starrating):
        self.title = title
        self.description = description
        self.rating = rating
        self.starrating = starrating

class MovieSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "rating", "starrating")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@app.route("/", methods=["GET"])
def home():
    return "<h1>Movie posts</h1>"

# GET
@app.route("/movies", methods=["GET"])
def get_movies():
    all_movies = Movie.query.all()
    result = movies_schema.dump(all_movies)

    return jsonify(result)

# GET ONE / "Show" route
@app.route("/movie/<id>", methods=["GET"])
def get_movie(id):
    movie = Movie.query.get(id)
    result = movie_schema.dump(movie)

    return jsonify(result)

# POST
@app.route("/movie", methods=["POST"])
def add_movie():
    title = request.json["title"]
    description = request.json["description"]
    rating = request.json["rating"]
    starrating = request.json["starrating"]
    
    new_movie = Movie(title, description, rating, starrating)

    db.session.add(new_movie)
    db.session.commit()

    movie = Movie.query.get(new_movie.id)
    return movie_schema.jsonify(movie)

# PUT / PATCH
@app.route("/movie/<id>", methods=["PATCH"])
def update_movie(id):
    movie = Movie.query.get(id)
    new_title = request.json["title"]
    new_description = request.json["description"]
    new_rating = request.json["rating"]
    new_starrating = request.json["starrating"]

    movie.title = new_title
    movie.description = new_description
    movie.rating = new_rating
    movie.starrating = new_starrating
    db.session.commit()

    return movie_schema.jsonify(movie)

# DELETE
@app.route("/del/movie/<id>", methods=["DELETE"])
def delete_movie(id):
    record = Movie.query.get(id)

    db.session.delete(record)
    db.session.commit()

    return jsonify({"message": "Movie deleted"})

if __name__ == "__main__":
    app.run(debug=True)