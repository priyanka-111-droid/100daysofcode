from flask import Flask, render_template
import requests 
import pandas as pd
app = Flask(__name__)

#getting all country codes and full names of countries to guess person's nationality
all_tables = pd.read_html('https://en.wikipedia.org/wiki/ISO_3166-2')
df = all_tables[0]



@app.route('/')
def home():
    return '<h1>Enter your name.</h1>'



@app.route('/guess/<name>')
def guess_api(name):

    parameters={
        "name":name 
    }
    #gender
    gender_response=requests.get(url="https://api.genderize.io",params=parameters)
    possible_gender=gender_response.json().get('gender')

    #age
    age_response=requests.get(url="https://api.agify.io",params=parameters)
    possible_age=age_response.json().get('age')

    #nationality
    nationality_response=requests.get(url="https://api.nationalize.io",params=parameters)
    #This will give us 2 letter country code
    nationality_code=nationality_response.json()['country'][0]["country_id"]

    for(index,row) in df.iterrows():
        if row["Entry (click to view codes)"]==nationality_code:
            #getting full country name from code
            possible_nationality=(row["Country name (using title case)"])


    
    return render_template("index.html",
    name=name.title(),
    gender=possible_gender,
    age=possible_age,
    nationality=possible_nationality
    ) 




if __name__ == "__main__":
    app.run(debug=True)

