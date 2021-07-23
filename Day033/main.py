#making a request to ISS(international space station) API
#requests module has to be installed
import requests


#get endpoint url from ISS documentation
#store in variable response
response=requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) #this gives us a response code object.


#Working with response codes
#Response codes tell you if our request worked or failed
#eg.404 response code means what you are looking for does not exist
#1XX:Hold on
#2XX:Here you go,everything was successful!
#3XX:Go away
#4XX:You screwed up
#5XX:I(as in server) screwed up,server down.


#To get only status code instead of whole object
print(response.status_code)

# if response.status_code!=200:
#     raise Exception("Bad response from ISS API")


# if response.status_code==404:
#     raise Exception("That resource does not exist.")
# elif response.status_code==401:
#     raise Exception("You are not authorized to access this data.") 
#But too many status codes ,so we cannot raise exception for all of them!
#Hence we use request module to raise exception

response.raise_for_status()

#GETTING ACTUAL DATA FROM API
data=response.json()
# print(data)

iss_pos=response.json()["iss_position"]
# print(iss_pos)

iss_pos_long=response.json()["iss_position"]["longitude"]
# print(iss_pos_long)

longitude=data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]
iss_position=(longitude,latitude)  #tuple
print(iss_position)



