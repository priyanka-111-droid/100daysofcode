# HTML and URL parsing in Flask and Higher Lower Game

# Theory

## Flask URL paths and the Flask debugger

Documentation:[routing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing) and [variable rules](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)

See flask_url.py

## Rendering HTML elements with Flask

See flask_html.py

# Exercise

1.Styling HTML using Flask

Under @app.route("/),

a)create another decorator @make_bold that will make text  bold.

b)create another decorator @make_emphasis that will make text emphasis.

b)create another decorator @make_underlined that will make text emphasis.

SOLUTION:flask_style.py

2.Advanced decorators

Create a logging_decorator() which is going to log the name of the function that was called, the arguments it was given and finally the returned output.

Expected Output
https://cdn.fs.teachablecdn.com/jA2ypes2RfuB0cuC41yd

HINT 1: You can use function.__name__ to get the name of the function.

HINT 2: You'll need to use *args

SOLUTION:dec_adv.py

# Project

[higher-lower]

Creating the higher lower game that we created in Day 14, but now with a real website.