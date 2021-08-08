# Selenium Webdriver and Game playing bot

## Theory

1.Installing and introduction to Selenium webdriver

Install [chrome](https://www.google.com/intl/en_uk/chrome/)

Install [chromedriver](https://chromedriver.chromium.org/downloads)

Use pip to install selenium

See [intro.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day048/Selenium-webdriver-and-game-playing-bot/intro.py)

2.How to find and select elements on a website using Selenium.

We can complete Day 47-Amazon tracker using Selenium-webdriver.

See [amazon.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day048/Selenium-webdriver-and-game-playing-bot/amazon.py)

Finding elements in other ways

See [find.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day048/Selenium-webdriver-and-game-playing-bot/find.py)

3.How to automate filling out forms and clicking buttons and links

See [interaction.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day048/Selenium-webdriver-and-game-playing-bot/interaction.py)

## Exercises

[Selenium Documentation](https://selenium-python.readthedocs.io/)

1.Go to the [Python docs website](https://www.python.org/) and get hold of all 'Upcoming Events'.You need to get 5 dates and their corresponding names and create a dictionary.

Sample output:

    {0: {'time': '2021-10-02', 'name': 'PyConTW 2021'}, 1: {'time': '2021-10-02', 'name': 'PyConTW 2021'}, 2: {'time': '2021-10-02', 'name': 'PyConTW 2021'}, 3: {'time': '2021-10-02', 'name': 'PyConTW 2021'}, 4: {'time': '2021-10-02', 'name': 'PyConTW 2021'}, 5: {'time': '2021-10-02', 'name': 'PyConTW 2021'}}

Hints:

* [List index has no attribute text error](https://stackoverflow.com/questions/49900117/python-selenium-list-object-has-no-attribute-text-error)

* [Nested dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension)

Solution:[48-1.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day048/Selenium-webdriver-and-game-playing-bot/Exercise/48-1.py)

2.Go to [wikipedia main page](https://en.wikipedia.org/wiki/Main_Page) and Use Selenium to get total number of articles in English located at top of the wikipedia page(eg.6,352,825) and print it out.

Solution:[48-2.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day048/Selenium-webdriver-and-game-playing-bot/Exercise/48-2.py)

3.Go to this [form sign up](http://secure-retreat-92358.herokuapp.com/) page and fill the form and click Sign up automatically.Note:this is NOT an actual sign up page,its just for testing purposes.

Solution:[48-3.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day048/Selenium-webdriver-and-game-playing-bot/Exercise/48-3.py)

## Project

[Cookie clicker](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day048/Selenium-webdriver-and-game-playing-bot/Project/cookieclicker.py)

* Go to the game website and familiarise yourself with how it works:http://orteil.dashnet.org/experiments/cookie/ (classic version)

* Create a bot using Selenium and Python to click on the cookie as fast as possible.

* Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one. You'll need to check how much money (cookies) you have against the price of each upgrade.

* After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second". 


