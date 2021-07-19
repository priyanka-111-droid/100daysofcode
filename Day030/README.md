# Errors,Exceptions and JSON Data Improving the Password

## Theory

1.Catching Exceptions using try catch except else finally pattern

See [main.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day030/Theory/main.py)

2.Raise your own Exceptions

See [own_exception.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day030/Theory/own_exception.py)

3.Introduction to [JSON](https://docs.python.org/3/library/json.html)

* JSON:Javascript Object Notation

* originally for javascript but now used for other fields like python

* One of the popular ways of transferring data especially across internet.

* JSON is made up of nested dictionaries and there is an inbuilt json library in python

* To write into json file:json.dump()

* To read from json file:json.load()

* To update into json file:json.update()

## Exercise

1.IndexError Handling Exercise

Question and Solution:[30-1.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day030/Exercise/30-1.py)

Issue:We've got some buggy code. Try running the code. The code will crash and give you an IndexError. This is because we're looking through the list of fruits for an index that is out of range.

Instructions:Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie"

Hints:

* You'll need to catch the IndexError exception.

* You'll need the try, except and else keywords.

2.KeyError Handling Exercise

Question and Solution:[30-2.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day030/Exercise/30-2.py)

Issue:We've got some buggy code, try running the code. The code will crash and give you a KeyError. This is because some of the posts in the facebook_posts don't have any "Likes".

Instructions:Use what you've learnt about exception handling to prevent the program from crashing.

Hints:

* You'll need to catch the KeyError exception.

* Posts without any likes can be counted as 0 likes.

## Project

1.Adding Exception Handling in NATO-alphabet Project from Day 26.

See [NATO-alphabet](https://github.com/priyanka-111-droid/100daysofcode/tree/main/Day030/Project/NATO-alphabet)

2.Improving Password Manager  from Day 29

See [password-manager-start](https://github.com/priyanka-111-droid/100daysofcode/tree/main/Day030/Project/password-manager-start)


