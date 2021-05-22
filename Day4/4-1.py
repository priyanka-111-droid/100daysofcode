#RANDOMIZATION

#pseudo random number generator(Khan acad)uses Mersenne twister
# import random
# random_integer = random.randint(1,10)  #print integer from 1 to 10
# random_float=random.random()     #prints float from 0 to 1
# random_fl=random.uniform(19,1)   #also 1,19
# print(random_fl)
# #can be used in love calc done in day 3
# love_score=random.randint(1,100)

# #CREATING OUR OWN MODULES
# import my_mod 
# print(my_mod.pi)

##########<<<<<<PROGRAM>>>###########
'''virtual coin toss program
by generating 0 or 1 and then print H or T'''
import random
if(random.randint(0,1)==1):
    print("Heads")
else:
    print("Tails")
