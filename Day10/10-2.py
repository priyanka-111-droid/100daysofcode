
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b 

first_num=float(input("What's the first number?:"))
#''' can be used as triple quoted string or docstring
op=input('''+
-
*
/
Pick one of operations above:
''')
sec_num=float(input("What is the next number?:"))
if op=="+":
    output=add(first_num,sec_num)
elif op=="-":
    output=subtract(first_num,sec_num)
elif op=="*":
    output=multiply(first_num,sec_num)
else:
    output=divide(first_num,sec_num)

print(f"{first_num} {op} {sec_num} = {output}")



