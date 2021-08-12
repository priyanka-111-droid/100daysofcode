from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style= "text-align:center">Hello world!</h1>'\
    '<p>This is a cat and dog fighting</p>'\
    '<br>'\
    '<img src="https://media.giphy.com/media/q1MeAPDDMb43K/giphy.gif" width=400 height=300>'



if __name__ == "__main__":
    app.run(debug=True)  