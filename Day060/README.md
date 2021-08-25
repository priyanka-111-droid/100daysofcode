# Make POST requests with Flask and HTML Forms

# Exercise

### HTML Forms Revision

Create a HTML Form in index.html so that when rendered as a webpage,you can see name and input field for name and password and submit button.

### Making the form work

1.We need our Flask server to be able to receive the data entered by the user.See if you can use the documentation below to figure out how to make our HTML form submit a "POST" request to the path "/login".

https://www.w3schools.com/tags/att_form_method.asp

https://www.w3schools.com/tags/att_form_action.asp

2.Once the form is submitted, we also need to catch this POST request in our server. To do this we first need to give each input in our form a name attribute.

3.Now we can create a decorator in our main.py that will trigger a method when it receives a POST request.

https://flask.palletsprojects.com/en/2.0.x/quickstart/#url-building

4.DIFFICULT CHALLENGE: See if you can use the Flask documentation below to figure out how to get hold of the name and password that was entered into the form and send it back to the client as a `<h1>`

Documentation:
https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object

HINT:
https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask


# Project

Let us make the form in the contact section of our blog site(Day 59) work.

1.Add a "/form-entry" route in main.py to receive data from the form:

2.CHALLENGE: Update the code in contact.html and main.py so that you print the information the user has entered into the form and return a `<h1>` that says "Successfully sent your message".

3.CHALLENGE: Combine the "/contact" route with "/form-entry" so that they are both under the route "/contact" but depending on which method (GET/POST) that triggered the route, handle it appropriately.

HINT: You can use request.method to check which method triggered the route.

https://flask.palletsprojects.com/en/2.0.x/quickstart/#http-methods

4.CHALLENGE: Instead of returning a `<h1>` that says "Successfully sent message", update the contact.html file so that the `<h1>` on the contact.html file becomes "Successfully sent message".

Hint : https://jinja.palletsprojects.com/en/3.0.x/templates/#if

6.Now we will send ourselves (website owner) an email when a user is trying to get in touch.

