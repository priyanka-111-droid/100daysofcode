# Flask URL paths and the Flask debugger
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


#Different routes using app.route decorator
@app.route("/bye")
def say_bye():
    return "Bye"


#Creating variable paths and converting path to specified data type
@app.route("/<name>")
def greet1(name):
    return f"Hello there {name}!"
    # return f"Hello there {name+12}!" will give TypeError
    

@app.route("/username/<name>/<int:number>")
def greet2(name,number):
    return f"Hey {name},you are {number} years old!"
   
    

if __name__ == "__main__":
    #Run app in debug mode to auto-reload
    app.run(debug=True)  


