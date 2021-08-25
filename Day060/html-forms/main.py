from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
   
#decorator for receiving POST request of form
@app.route("/login",methods=["POST"])
def receive():
    name= request.form["yourName"]
    password=request.form["yourPassword"]

    return f'<h1>Name:{name},Password:{password}</h1>'



if __name__ == "__main__":
    app.run(debug=True)  