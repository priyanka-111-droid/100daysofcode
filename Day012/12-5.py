###<<<PROJECT>>>###
'''
Number Guessing Game Objectives:
1.Include an ASCII art logo from 
2.Allow the player to submit a guess for a number between 1 and 100.
3.Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
4.If they got the answer correct, show the actual answer to the player.
5.Track the number of turns remaining.
6.If they run out of turns, provide feedback to the player. 
7.Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

'''
import random 
from art import logo

 
def guessing(tries):
    guess=int(input("Enter number from 1 to 100 :"))
    #in case,user enter number less than 1 or more than 100,
    #while loop forces user to enter number until number is from 1 to 100
    while(guess<1 or guess>100):
         guess=int(input("Enter number from 1 to 100 :"))

    if(guess==actual):
        print(f"Congrats,you got it!!..Answer was {actual}")
    elif(guess<actual):
        print("Too low")
        tries=tries-1
    elif(guess>actual):
        print("Too high")
        tries=tries-1

    return tries 


print(logo)
print("Welcome to the Number guessing game!!")
actual=random.randint(0,100)
level=input("Choose e for easy mode(10 guesses) and h(5 guesses) for hard mode :")

if level=='e':
    tries=10
    while(tries!=0):
        tries=guessing(tries)
        if(tries==10):  #answer achieved at first attempt(no tries used),so break loop
            break 
        else:
            print(f"You have {tries} tries left")
    if(tries==0):
        print(f"Sorry,you have no attempts left,better luck next time...answer was {actual}")
    
elif level=='h':
    tries=5
    while(tries!=0):
        tries=guessing(tries)
        if(tries==5):
            break 
        else:
            print(f"You have {tries} tries left")
    if(tries==0):
        print(f"Sorry,you have no attempts left,better luck next time,the answer was {actual}")
   





