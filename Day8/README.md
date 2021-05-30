# Review:
1. Create function called greet 
2. print 3 statements in greet 
3. call greet()

        def greet():
            print("Hi Angela here!")
            print("How do you do Jack Bauer?")
            print("Isn't the weather nice today?")

        #calling function
        greet()

# Function that allows 1 input

        def greet_with_name(name): #name is parameter 
            #using f strings to connect input and 
            #existing string

            print(f"Hi {name} here")
            print(f"How do you do {name}?")
            print("Isn't the weather nice today?")

        #calling function
        greet_with_name("Hanna") #Hanna is argument

* name : **parameter**,used inside function

* "Hanna": **argument**,actual piece of data being passed
* When you call the function greet_with_name(),arguments is passed into parameters

# Function with more than 1 input

## Using Positional Arguments

        def greet_with_name(name,location):

            print(f"Hi {name} here")
            print(f"What is it like in {location}?")


        greet_with_name("Hanna","Singapore") 
        #by default,Hanna is assigned to name and 
        #Singapore assigned to location

        greet_with_name("Singapore","Hanna")
        #the above line will print a senseless sentence


* This is default way of calling function using positional argument as we did not specify which argument should get assigned to which parameter

* So, 1st argument->1st parameter and 2nd argument->2nd parameter

## Using Keyword Arguments

        def greet_with_name(name,location):
            print(f"Hi {name} here")
            print(f"What is it like in{location}?")

        greet_with_name(name="Hanna",location="Singapore") 
        greet_with_name(location="Singapore",name="Hanna") 

        #BOTH of the above function calls will 
        #result in SAME OUTPUT

* Using keyword arguments means you can change order of arguments passed into the parameters


# Exercises

## 1.Paint Area Challenge:

Instructions:

You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5

But because you can't buy 1.6 of a can of paint, the result should be rounded up to 2 cans.

Sample Input:

        test_h=3
        test_w=9

Sample Output:

        You'll need 6 cans of paint.


Hint:
* To round up a number:
https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python

* Make sure you name your function/parameters the same as when it's called on the last line of code.

Solution: [8-1.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day8/8-1.py)

## 2.Prime Number Checker

Instructions:

Prime numbers are numbers that can only be cleanly divided by itself and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

Sample Input:
        73
Sample Output:
        It's a prime number

Hint:
* Remember the modulus:
https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python

* Make sure you name your function/parameters the same as when it's called on the last line of code.

Solution: 8-2.py

# Project

## 1.Caesar Cipher-part 1(encode)
Fork the repl or copy starting code from repl [here](https://replit.com/@appbrewery/caesar-cipher-1-start)

Instructions:

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        text = input("Type your message:\n").lower()

        shift = int(input("Type the shift number:\n"))

TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
e.g. 

text = "hello"

shift = 5

cipher_text = "mjqqt"

print output: "The encoded text is mjqqt"

text="zulu"

shift = 5

cipher_text = "ezqz"

print output: "The encoded text is ezqz"

Hint: How do you get the index of an item in a list:
https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list


TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.Use keyword arguments

Solution: 8-3.py

## 2.Caesar cipher-part 2(decode)

Fork the repl or copy starting code from repl [here](https://replit.com/@appbrewery/caesar-cipher-2-start)

TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift 
  amount and print the decrypted text.  
  e.g. 

  cipher_text = "mjqqt"

  shift = 5

  plain_text = "hello"

  print output: "The decoded text is hello" 


TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call
 the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* 
 decrypt a message.

Solution: 8-4.py

## 3.Caesar cipher-part 3(reorganize)

Fork the repl or copy starting code from repl [here](https://replit.com/@appbrewery/caesar-cipher-3-start)


* TODO-1: Combine the encrypt() and 
decrypt() functions into a single 
function called caesar().

* TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

Solution: 8-5.py

## 4.Caesar cipher-part 4(improve user experience)

Fork the repl or copy starting code from repl [here](https://replit.com/@appbrewery/caesar-cipher-4-start)

* TODO-1: Import and print the logo from art.py when the program starts.

* TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
Try running the program and entering a shift number of 45.
Add some code so that the program continues to work even if the user enters a shift number greater than 26. 

  Hint: Think about how you can use the modulus (%).

* TODO-3: What happens if the user enters a number/  symbol/space?
Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
e.g. start_text = "meet me at 3"

  end_text = "•••• •• •• 3"

* TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
e.g. Type 'yes' if you want to go again. Otherwise type 'no'.

  If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?

  Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

Solution: 8-6.py






