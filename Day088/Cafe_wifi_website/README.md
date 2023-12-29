# Cafe and Wifi website

## Instructions

- On day 66, we create an API that serves data on cafes with wifi and good coffee. 
- Today, you're going to use the data from that project to build a fully-fledged website to display the information.Included in this assignment is an SQLite database called cafes.db that lists all the cafe data.
- Using this database and what you learnt about REST APIs and web development, create a website that uses this data. It should display the cafes, but it could also allow people to add new cafes or delete cafes.
- Demo example:
https://laptopfriendly.co/london


## Approach:

- Start with day 66 code.
- **Get all cafes** - main.py, function home(), render index.html and pass parameter cafes.

- **Get random cafe** - main.py,function get_random_cafe(), render get_random.html,pass parameter random_cafe.Now update link in Navbar(base.html) to get a random cafe using url_for.

- **Add cafe** - main.py, function add_a_cafe(),
        - Initially, display or render add_cafe form(add_cafe.html).This is the default GET method.
        - Once form gets submitted(if request.method=='POST'),capture all inputs from form
        (eg. `request.form.get("name")`) and then add new cafe into database. Redirect to home page
        once that is done.
        - Now update link in Navbar(base.html) to add cafe using url_for.

- **Update coffee price**  - since this option has to be given for every individual coffee price, provide it as a link in index.html.When clicked, it goes to update_price function in main.py and passes parameter num which holds cafe_id.This helps us identify id of cafe that has to be updated.
    - Initially,after being clicked, get the value of num and cafes and display the update html 
    form.(update.html) and pass parameters num and cafes to that form.
    - Once form gets submitted(if request.method=='POST'),capture the new price and update the 
    cafe having that id with new price. Redirect to home page once that is done.

- **Delete cafe**  - since this option has to be given for every individual coffee price, provide
    it as a link in index.html.When clicked, it goes to delete_cafe function in main.py
    and passes parameter num which holds cafe_id.This helps us identify id of cafe that has 
    to be deleted.
    - Initially,after being clicked, get the value of num and delete the cafe from database.

- **Search cafe based on location user enters**  - Make search field and button in navbar in `base.html` part of a small form.When user clicks 'search' button after typing location, action attribute of form will lead it to function find_a_cafe() in main.py.
        - Initially, display just index.html or homepage since search bar is present in home page only.
        - After form gets submitted(user types location and clicks 'search' button), get new location and 
        search for that location in all cafes.(search.html) and pass parameters location,cafes to search.html form.


## Remember

- When using Jinja templating, you don't need to use double curly braces ({{ }}) inside the {% if %} statement.The {% if %} statement already expects an expression, so you don't need the double curly braces inside it.

- Make sure that the name attributes in your HTML form match the attribute names in your Flask route (request.form['name'], request.form['img_url'], etc.). 

- To capture form input checkbox, we added the name="has_sockets" attribute to the checkbox. This is the name that will be used to retrieve the checkbox value in your Flask route.I also added {% if request.form['has_sockets'] %} checked {% endif %} to the input tag. This is a Jinja template condition that checks if the has_sockets value is present in the request.form. If it is, the checked attribute will be added, indicating that the checkbox should be checked. Use `has_sockets = request.form.get("has_sockets") == 'on'  # Check if the checkbox is checked` in Flask route.

- Implementing Search cafe based on location functionality in website. Tested with location 'Peckham'.All cafes location in 'Peckham' were displayed. For a location that does not exist in our database, use flag variable and setit to False in beginning.
`{% set is_there_any_location = False %}`
If location is there, `{% set is_there_any_location = True %}` and display cafe details.



## Future implementation

- How to display map_url of location? Not working with iframe or embed tag.
- Ability to update all attributes of cafe, not just coffee price.
