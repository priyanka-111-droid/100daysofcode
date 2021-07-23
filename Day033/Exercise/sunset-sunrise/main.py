import requests
from datetime import datetime

MY_LAT=51.507531
MY_LONG=-0.127758

parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
# print(data)

#to get actual hour in 24 hour clock of sunrise time
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
#to get actual hour in 24 hour clock of sunset time
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise) #12 hour format by default.
#to get 24 hour format of sunrise,use "formatted" parameter and set it to 0


print(sunrise) 
print(sunset) 


#to get time now
time_now=datetime.now()
print(time_now.hour) #24 hour format

