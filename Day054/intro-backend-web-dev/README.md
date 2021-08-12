# Introduction to Backend Web development with Python

# Theory

## Components of web development:

* See [intro.md](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Theory/intro.md) for more details.

## __name__ and __main__

* Documentation:[__name__](https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes) and [__main__](https://docs.python.org/3/library/__main__.html)

* See [name_and_main](https://github.com/priyanka-111-droid/100daysofcode/tree/main/Day054/intro-backend-web-dev/Theory/name_and_main)

## First class functions,closures and python decorators

1.First class functions,closures(needed before learning decorators):[first-class-func.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Theory/first-class-func-and-decorators/first-class-func.py)

2.Decorators introduction:[dec1.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Theory/first-class-func-and-decorators/dec1.py)

Examples:

* Adding delay to a function:[dec2.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Theory/first-class-func-and-decorators/dec2.py)

* Decorators and args and kwargs:[dec3.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Theory/first-class-func-and-decorators/dec3.py)

* Decorators and classes:[dec4.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Theory/first-class-func-and-decorators/dec4.py)

# Exercises

## Creating our first web server with Flask

* [Install Flask](https://pypi.org/project/Flask/)

* [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

* Make sure the name of python file DOES NOT conflict with name of framework.

* [Run Flask using environment variables](https://stackoverflow.com/questions/51119495/how-to-setup-environment-variables-for-flask-run-on-windows)

* Run Flask using Python built in attributes like [__name__](https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes) and [__main__](https://docs.python.org/3/library/__main__.html)

SOLUTION:[intro_flask.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Exercise/intro_flask.py)

## Creating our own decorator

time.time() will return the current time in seconds since January 1, 1970, 00:00:00

Try running the starting code to see the current time printed.If you run the code after a while, you'll see a new time printed.

e.g. 

first run:1598524371.736911

second run:1598524436.357875

The time difference = second run - first run

64.62096405029297

(approx 1 minute)

Given the above information, complete the code exercise by printing out the speed it takes to run the fast_function() vs the slow_function(). You will need to complete the speed_calc_decorator() function.

HINT: You can use function.__name__ to get the name of the function

SOLUTION:[dec_practice.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Exercise/dec_practice.py)

## Handling Exceptions using decorators

You can make sure that some family of exceptions are handled, without have to enter a try block for each function you need to check it. Then you can log or stop the execution of the program.

1.Define 4 functions:

divide(a,b) : prints a/b

key_of_dictionary(a_dictionary,non_existent_key) : prints value of a key 

element_of_list(fruit_list,index): prints fruit at a particular index from list of fruits

string_and_int(text,number) : adds a number to a string and prints the result

2.Define a decorator function error_handler with a try catch block that will print name of Exception and name of function that the Exception occurs in.

3.Call the below functions:

    divide(20,0)
    key_of_dictionary( {"key":"value"},"key2")
    element_of_list(["apples","bananas","oranges"],4)
    string_and_int("abcd",5)

4.Sample output:

        Exception:ZeroDivisionError
        Exception in divide function
        Exception:KeyError
        Exception in key_of_dictionary function
        Exception:IndexError
        Exception in element_of_list function
        Exception:TypeError
        Exception in string_and_int function

HINT:https://stackoverflow.com/questions/1483429/how-to-print-an-exception-in-python and [dec3.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Theory/first-class-func-and-decorators/dec3.py)

SOLUTION:[dec_excep.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day054/intro-backend-web-dev/Exercise/dec_excep.py)

