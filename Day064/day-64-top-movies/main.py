from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import requests

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collections.db"
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class RateMovieForm(FlaskForm):
    your_rating = StringField('Your rating', validators=[InputRequired()])
    your_review = StringField('Your review', validators=[InputRequired()])
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
    number = int(num)
    all_movies = db.session.query(Movie).all()
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_id = num
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = form.your_rating.data
        movie_to_update.review = form.your_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',num=number,movies=all_movies, form=form)


if __name__ == '__main__':
    app.run(debug=True)
