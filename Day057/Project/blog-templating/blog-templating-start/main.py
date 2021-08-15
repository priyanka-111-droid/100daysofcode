from flask import Flask, render_template
from post import Post

app = Flask(__name__)
p=Post()
modified_blog=p.return_blog()


@app.route('/')
def home():
    return render_template("index.html",posts=modified_blog)


@app.route("/post/<int:num>")
def get_post(num):
    return render_template("post.html",posts=modified_blog,num=num)


if __name__ == "__main__":
    app.run(debug=True)
