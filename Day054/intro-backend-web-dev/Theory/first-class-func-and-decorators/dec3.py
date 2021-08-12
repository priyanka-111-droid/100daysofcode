#PYTHON DECORATORS ADVANCED EXAMPLE(with args and kwargs):

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args,**kwargs)

    return wrapper_function


@decorator_function
def display():
    print("Display function ran")


@decorator_function
def display_info(name,age):
    print(f"display_info ran with arguments ({name},{age})")


display()
display_info("John", 25)


