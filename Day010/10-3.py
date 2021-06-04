def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b 

first_num=float(input("What's the first number?:"))

op={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

for symbol in op:
    print(symbol)

operation_input=input("Pick one of the operations above:")
sec_num=float(input("What is the next number?:"))

calculation_function=op[operation_input]  #tap into dictionary op and get the operations to be done

output=calculation_function(first_num,sec_num) 


print(f"{first_num} {operation_input} {sec_num} = {output}")



