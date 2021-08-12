#PYTHON DECORATORS EXAMPLE
#Decorator function is a function that wraps another function and gives it another functionality or additional functionality.
#In the below example,the functionality is to add delay to a function.

import time

def delay_decorator(function):
    def wrapper_func():
        time.sleep(2)
        #Do something before 
        function()
        #Do something after

    return wrapper_func


# We can write @delay decorator to decorate function written below it
@delay_decorator 
def say_hello():
    print("Hello")

@delay_decorator 
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")

#calling function
say_hello()


#We can also write delay_decorator({name of function to be decorated}) instead of the @ syntax.
decorated_function=delay_decorator(say_greeting)
decorated_function()

