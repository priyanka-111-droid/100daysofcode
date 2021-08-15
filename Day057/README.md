# Templating with Jinja in Flask applications

# Theory

Jinja is templating language for Python.It is already bundled with Flask and there is no need to install Jinja separately.When we use {{}},the expression inside is evaluated.

[Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/)

## Multiline statements with Jinja

If we wanted to use if statements and for loops,we would need to use slightly different markup.

See [multiline-jinja]()

## URL Building with Flask

See [url-building documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/#url-building)

# Exercise

## Using Jinja to produce dynamic HTML pages and generating dynamic footers

See [here]https://updateyourfooter.com/).We will be updating the footer of a HTML page to show the current year using python instead of javascript or PHP.It should display "Copyright CURRENT_YEAR.Built by YOUR_NAME"

SOLUTION: [dynamic-footer]

## Combine Jinja Templating with APIs

* [Genderize API](https://genderize.io/)

* [Agify API](https://agify.io/)

* [Nationalize API](https://nationalize.io/)

* Turn this into a dynamic Flask application.Set up a new route '/guess/{NAME}'.

* When we enter a name,it should display our possible gender,age and nationality.

* The nationalize API returns [ISO 2 letter country codes](https://en.wikipedia.org/wiki/ISO_3166-2) instead of the full country name.So we have used pandas to read HTML tables from [here](https://en.wikipedia.org/wiki/ISO_3166-2) and get the full country name from country code.See [Reading HTML tables using pandas](https://pbpython.com/pandas-html-table.html)

SOLUTION:[using-apis]()

# Project

[Blog posts]()






