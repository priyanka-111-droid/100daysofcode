####<<<DECORATORS>>>####
# A decorator is a function that takes another function as an argument,adds some functionality and returns another function

#Recap:first class function
def outer_func(message):
    def inner_func():
        print("Message :",message)
    
    #no () as we don't want this function to execute
    return inner_func


greeting=outer_func("Hi!")
greeting()
goodbye=outer_func("Bye!")
goodbye()




#Now modifying above code sample to a decorator:
#instead of passing message,we will pass function called original_function
def decorator_function(original_function):
    def wrapper_function():
        # print("Message :",message)
        #instead of printing message,we will execute original function and return it
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function()

    return wrapper_function

def display():
    print("display function ran")


#FIRST WAY TO DECORATE A FUNCTION AND EXECUTE IT
decorated_display=decorator_function(display)
decorated_display()


#SECOND WAY TO  DECORATE A FUNCTION AND EXECUTE IT(using @ symbol)
@decorator_function
def another_display():
    print("Another display function ran")


another_display()