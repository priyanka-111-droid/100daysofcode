import requests
from datetime import datetime 
from dotenv import load_dotenv 
import os

load_dotenv()

NUTRI_APP_ID=os.getenv("NUTRI_APP_ID")
NUTRI_API_KEY=os.getenv("NUTRI_API_KEY")
SHEETY_POST_URL=os.getenv("SHEETY_POST_URL")
BEARER_AUTH_TOKEN=os.getenv("BEARER_AUTH_TOKEN")

BASE_URL="https://trackapi.nutritionix.com/"
EXERCISE_URL=f"{BASE_URL}/v2/natural/exercise"


#Nutritionix
GENDER=os.getenv("GENDER")
WEIGHT=os.getenv("WEIGHT")
HEIGHT=os.getenv("HEIGHT")
AGE=os.getenv("AGE")

exercise_params={
    "query":input("Enter your exercises :"),
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}
headers={
    "x-app-id":NUTRI_APP_ID,
    "x-app-key":NUTRI_API_KEY,
    "x-remote-user-id":"0"
}
response1=requests.post(url=EXERCISE_URL,json=exercise_params,headers=headers)
exercise_data=response1.json()


#google sheets
today_date=datetime.now().strftime("%d/%m/%Y")
now_time=datetime.now().strftime("%X")
bearer_headers={
    "Authorization":f"Bearer {BEARER_AUTH_TOKEN}",
}
for exercise in exercise_data["exercises"]:
    sheet_inputs={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response2=requests.post(url=SHEETY_POST_URL,json=sheet_inputs,headers=bearer_headers)
    print(response2.text)

