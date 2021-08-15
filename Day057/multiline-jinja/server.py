from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello world</h1>'

@app.route("/blog")
def blog():
    #fetch blogs from url of the API
    BLOG_URL="https://api.npoint.io/09b8316e15e0e21878a0"
    response=requests.get(url=BLOG_URL)
    all_posts=response.json()
    return render_template("index.html",posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)