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
print(data)

