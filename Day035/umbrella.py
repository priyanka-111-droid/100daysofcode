import requests,os

api_key=os.environ.get('API_KEY')
MY_LAT=19.075983
MY_LONG=72.877655

parameters={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

#Since we only want hourly data ,we are excluding rest of the data.
response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
data=response.json()
will_rain=False
#since we want for 12 hours
# for hour in range(12):
    # condition_code=(data["hourly"][hour]["weather"][0]["id"])

#more pythonic way is to use slice
weather_slice=data["hourly"][:12] # for 0 to 11
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if(int(condition_code)<700):
        will_rain=True    

if(will_rain):
    print("Bring an umbrella")




