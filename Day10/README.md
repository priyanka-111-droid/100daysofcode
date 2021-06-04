# Functions with outputs

    def my_function():
        return 3*2

    #returned value will replace part of code where function was called
    #returned value has to be stored in another variable,output.

    output=my_function()
    print(output)

    #you can also print this directly without storing in another variable
    print(my_function())

## Task 1:

Input first name and last name as parameters and convert strings to title case(first letter of each word capital)

Hint:
See [here](https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python)

eg.
MARY SMITH,mary smith,MaRy SmiTH --> Mary Smith

Solution: [task1.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day10/task1.py)

## Task 2:

In task 1,make the following changes

* In function,format_name(first_name,last_name) make sure that user does not enter empty first name or last name,if they do,print "You didn't provide valid inputs."

* Also make program user defined (user should be able to enter their first name and last name)

* Try using a variable output to store returned value and also try directly printing value WITHOUT use of variable.

Hint:Any statement after return,does not get executed.BUT,you can use multiple returns with the help of if else.

Solution: [task2.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day10/task2.py)

# Exercise 

1.Days in Month:

Fork repl from [here](https://replit.com/@appbrewery/day-10-1-exercise)

Solution: 10-1.py

# Project:

Calculator 

## Part 1:Using Functions and if else 

What should output look like?

        What's the first number?:12
        +
        -
        *
        /
        Pick one of operations above:
        -
        What is the next number?:11
        12.0 - 11.0 = 1.0

Steps:

* Define 4 functions add(),subtract(),multiply(),divide() that accept 2 parameters(2 numbers) and return the output
after performing operation.

* Input first number as float,input operation to be performed out of (+,-,*,/) as string and input second number as float.

* Use if else and based on operation chosen,pass parameters to respective functions and store result in output variable

* print final result using f string that shows operation being performed.
eg. 10.0 + 3.0 =13.0 (this has to be printed on output screen)

Solution:10-2.py

## Part 2:Using functions and dictionaries

* Replace operations with a dictionary showing symbol: operation name eg. +:"add"

* use for loop to print operations available for user to choose from.

* Input operation to be performed as another variable operation_input

* Replace if else with dictionary

* change f string to print operation correctly.

Solution: 10-3.py

## Part 3:Adding art.py,using while loops

* TODO-1:add import statement from art.py

* TODO-2:print logo

* TODO-3:define while loop using flag terminate and if user wishes to continue program,make output as first number else exit while loop and make sure you put while loop AFTER first number input.

* TODO-4:put entire code from logo till end of while loop into function calculator()

* TODO-5:call function calculator()

Solution: 10-4.py











