from flask import Flask,render_template
import requests

BLOG_API="https://api.npoint.io/bd293e18554ba56ad1aa"

response=requests.get(url=BLOG_API)
all_blogs=(response.json())

app=Flask(__name__)


@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html",posts=all_blogs)

@app.route('/post.html/<int:num>')
def get_post(num):
    return render_template("post.html",posts=all_blogs,num=num)


@app.route('/about.html')
def get_about():
    return render_template("about.html")

@app.route('/contact.html')
def get_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True,host='localhost',port='5000')


