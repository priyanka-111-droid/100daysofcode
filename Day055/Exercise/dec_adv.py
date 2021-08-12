def logging_decorator(original_func):
    def wrapper_func(*args):
        print(f"Function {original_func.__name__}{args} is being called")
        result=original_func(args)
        print(f"It returned :{result}")

    return wrapper_func

@logging_decorator
def adding(args):
    s=0
    for number in args:
        s=s+number

    return s 
    

adding(2,3,4)
adding(7,8)



