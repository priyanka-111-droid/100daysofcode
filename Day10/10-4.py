#TODO-1:add import statement from art.py
from art import logo

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b 

#TODO-4:define function calculator()
def calculator():

    #TODO-2: print logo
    print(logo)

    first_num=float(input("What's the first number?:"))
    #TODO-3:define while loop using flag terminate and if user wishes to continue program,make output as first number 
    #else exit while loop


    terminate =False
    while not terminate:
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

        # if calculator is to be continued,output becomes first number
        #Hence no need to input first number again

        if(input("Press y to continue with {output} or press n to end program ")=='y'):
            first_num=output 
        else:
            print("Thank you for using our calculator!!")
            terminate=True


#TODO-5:calling function calculator
calculator()



