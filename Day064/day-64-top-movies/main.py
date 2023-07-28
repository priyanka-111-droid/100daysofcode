from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("MOVIE_API"); 


db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collections.db"
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class RateMovieForm(FlaskForm):
    rating = StringField('Your rating', validators=[InputRequired()])
    review = StringField('Your review', validators=[InputRequired()])
    submit = SubmitField('Submit')


class AddMovie(FlaskForm):
    your_movie_name = StringField('Your movie name', validators=[InputRequired()])
    submit = SubmitField('Submit')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

# CREATE RECORD
# with app.app_context():
#     new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#     db.session.add(new_movie)
#     db.session.commit()



@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html",movies=all_movies)


@app.route('/edit/<num>',methods=["GET","POST"])
def edit(num):
    movie_id = num
    all_movies = db.session.query(Movie).all()
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',num=movie_id,movies=all_movies, form=form)


@app.route('/delete/<num>',methods=["GET","POST"])
def delete(num):
    movie_id = num
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add',methods=["GET","POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        parameters = {
            "api_key":API_KEY,
            "query":form.your_movie_name.data
        }
        search_url = "https://api.themoviedb.org/3/search/movie"
        response = requests.get(url=search_url,params=parameters)
        response.raise_for_status()
        data = response.json()['results']
        return render_template("select.html",data=data)
    return render_template("add.html",form=form)

@app.route('/get_movie/<num>',methods=["GET","POST"])
def get_movie(num):
    movie_id=num 
    get_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    parameters = {
        "api_key":API_KEY
    }
    response = requests.get(url=get_details_url,params=parameters)
    response.raise_for_status()
    movie_json = (response.json())
    # with app.app_context():

    #temporary rating and review
    new_movie = Movie(
        title = movie_json['original_title'],
        img_url =  f"https://image.tmdb.org/t/p/w500/{movie_json['poster_path']}",
        year=movie_json['release_date'].split('-')[0],
        description = movie_json['overview'],
        rating = 3,
        ranking=3,
        review='very good'
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", num=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
