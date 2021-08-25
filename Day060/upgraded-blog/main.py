from flask import Flask,render_template,request
import requests
from dotenv import load_dotenv
import os,smtplib

MY_EMAIL=os.getenv('MY_EMAIL') 
PASSWORD=os.getenv('PASSWORD')

BLOG_API="https://api.npoint.io/bd293e18554ba56ad1aa"

response=requests.get(url=BLOG_API)
all_blogs=(response.json())

app=Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html",posts=all_blogs)

@app.route('/post.html/<int:num>')
def get_post(num):
    return render_template("post.html",posts=all_blogs,num=num)


@app.route('/about.html')
def get_about():
    return render_template("about.html")

# @app.route('/contact.html')
# def get_contact():
#     return render_template("contact.html")

@app.route('/contact',methods=["GET","POST"])
def get_contact():

    if request.method == "POST":
        data = request.form
        # print(data["yourName"])
        # print(data["yourEmail"])
        # print(data["yourPhone"])
        # print(data["yourMessage"])

        #sending an email
        name=data["yourName"]
        email=data["yourEmail"]
        phone=data["yourPhone"]
        message=data["yourMessage"]

        connection=smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:User details\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}"
        )

        connection.close()



        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



if __name__ == "__main__":
    app.run(debug=True,host='localhost',port='5000')


