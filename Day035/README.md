# Keys,Authentication,Environment variables

## API Key:

Most APIs provide a free tier that allows us to test applications and for beginners.But when your application or service has a lot of users then you will have to pay in order to use the API.How to prevent people from abusing this free tier?

This is done with the help of API key.It is almost like the personal account number and password.This is how API provider tracks how much you are using their API and to authorize access and deny access once you have gone over the limit.

## Environment variables

These help in convenience and security.
Eg.to make sure our API keys remain secure. 

1.To create environment variables,open  the terminal and write,

        export API_KEY={value of api key between double quotes}

NOTE:For Windows,instead of export you need to write set.

2.Now in order to use this environment variable,you need to import os module.

        api_key=os.environ.get("API_KEY)


## Exercise

### 1.Testing our API key

* Create a free account on openweathermap.org.Get your own api key under My API keys and change the name of the key to whatever you wish.

* Now under the API section,in weather API,go to the API doc under Current weather data.

* Now copy the link of API call into a new tab and replace {city name} with your city and {API key} with your own API key.You should get the result in the form of weather data.

### 2.One call API

* Go to API doc for One call API.
Make an API request from your python editor to the one call API and locate hourly forecast for next 48 hours in the json response that you get back.

* See one_call_api.py

* To locate hourly forcast,copy the huge json response into [http://jsonviewer.stack.hu/](http://jsonviewer.stack.hu/) and click viewer.This will organize the json and now we can easily get the hourly data.

### 3.Check if it will rain in next 12 hours

For weather condition codes(ids) see [here](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)

Look through the data we get,get hold of first 12 items from hourly list.In each item,go to first item in weather list and get its condition id.If any of those ids are less than 700,print Bring an umbrella.

Hints:

1.Using python [slice](https://stackoverflow.com/questions/509211/understanding-slice-notation)

See umbrella.py


