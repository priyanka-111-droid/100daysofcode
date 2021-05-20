'''
Rock-paper-scissors:user vs computer
'''
import random
#can also try import random as rd
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images=[rock,paper,scissors]
user=int(input("What do you choose?Type 0 for Rock,1 for paper,2 for scissors"))
print(images[user])

#computer randomly selects any integer from 0 to 2
computer=random.randint(0,2)
print(f"Computer chose {computer}")
print(images[computer])


#Method 1 - long method
# if(user==0):
#     if(computer==0):
#         print("Nobody wins")
#     elif(computer==1):
#         print("Computer wins")
#     else:
#         print("User wins")
# elif(user==1):
#     if(computer==0):
#         print("User wins")
#     elif(computer==1):
#         print("nobody wins")
#     else:
#         print("Computer wins")
# elif(user==2):
#     if(computer==0):
#         print("Computer wins")
#     elif(computer==1):
#         print("User  wins")
#     else:
#         print("Nobody  wins")
# else:
#     print("User has entered invalid choice!")

#Method 2- shorter way!

if user > 2:
    print("Invalid Choice!")
else:
    if (user == 0 and computer == 2) or (user == 2 and computer == 1) or (user == 1 and computer == 0):
        print("You won!")
    elif user == computer:
        print("It's a tie!")
    else:
        print("You lose!")


#Mistakes:
#Learn how to use shorter if else codes
