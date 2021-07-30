# Capstone Flight Deal Finder 

## APIs needed:

Google Sheet Data Management - https://sheety.co/

Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/

Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

Twilio SMS API - https://www.twilio.com/docs/sms

## Program requirements:

1.Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

2.Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

3.If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

4.The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. 