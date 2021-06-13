#using function as input to another function

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


def calculator(n1,n2,func):
    return func(n1,n2)

result=calculator(2,3,add)

print(result)

#in this case calculator() is a higher order function
#since it takes another function as input
#and it works with it inside body of function
