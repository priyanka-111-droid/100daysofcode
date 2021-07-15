#can use unlimited number of keyword arguments
#with help of **kwargs

def calculate(n,**kwargs):
    print(kwargs)
    # print(type(kwargs)) #class dict

    #printing key and value for all items
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)

    #printing value of key add
    # print(kwargs["add"])

    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)


calculate(2,add=3,multiply=5)
#basically converts to dictionary having keys and values

