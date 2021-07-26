# Habit tracking Project,API post requests and Headers

## HTTP requests

We have been using GET up till now in the form of requests.get() to request data from external system and they give it to us in the form of response.But 4 other types of requests exist:

1.POST:requests.get()

Here we give external system some data but we are not that interested in response.We just wish to know if it was successful or not.

Eg.If we wanted to save a piece of data in Google sheets,we use Google sheets API to POST data into Google sheets.

PUT:requests.put()

Used to update a piece of data in external system.

Eg.update data in Google sheets

DELETE :requests.delete()

To delete data in external system.

## Header

We are providing API Key authentication in the header for this project instead of providing it as a parameter as we used to do so previously.This is much more secure.

## Project:Habit tracker

We will post habit tracking data to Pixela to be tracked in our graph.Follow the How do I use Pixela? section in the website.

[Pixela](https://pixe.la/)

[Pixela API](https://docs.pixe.la/)

[strftime() method](https://www.w3schools.com/python/python_datetime.asp)

