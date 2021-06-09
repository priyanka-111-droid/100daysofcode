


# 1.import art and game_data
from art import logo
from art import vs
from game_data import data

#14.from os import system and name to clear screen
from os import system,name


#15.to clear screen
#we will be calling this function before we show next 2 comparisions each time user wins
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



#2.print(logo)
print(logo)

#3.import random
import random 

#10.deciding max followers
def check_max(A,B):
    if(A['follower_count']>B['follower_count']):
        return 'A'
    else:
        return 'B'


#12.create function game()
def game():
    #11.while loop and put score OUTSIDE loop else it will keep becoming 0 if inside loop
    score=0
    terminate=False 
    while not terminate:

        #4.data is a LIST with many dictionaries,so use random.choice() to select A from list.
        A=random.choice(data)

        #5.To access the value of each key  in  dictionary,remember you DO NOT print follower count from the dictionary...
        # print(f"{A['name']}")
        print(f"{A['name']},a {A['description']},from {A['country']}")

        #6.print vs symbol
        print(vs)

        #7.Do same thing for B.
        B=random.choice(data)
        #making sure that random.choice() does not choose same person again..
        while(A==B):
            B=random.choice(data);

        print(f"{B['name']},a {B['description']},from {B['country']}")

        #8.Ask user
        user=input("Who has more followers?Type 'A' or 'B' :").upper()


        #9.Check user with value of 'follower_count' key in A and B dictionaries
        result=check_max(A,B)
        if(result==user):
            print("Congrats,you won!!\n")
            score+=1
            #16.calling clear function
            clear()
        else:
            print(f"You lost sorry...final score is {score}")
            if(input("Press y to restart the game or n to quit :")=='n'):
                print("Thank you for playing!")
                terminate=True
            else: 
                #when restarting ,set score to 0,clear previous outputs and display logo again..
                score=0 

                #16.calling clear()
                clear()
                print(logo)



#13.print introduction to user and call game()
print("Welcome to the higher lower game!!")
game()











