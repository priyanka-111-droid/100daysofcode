#RANDOMIZATION

#pseudo random number generator(Khan acad)uses Mersenne twister
# import random
# random_integer = random.randint(1,10)
# random_float=random.random()
# random_fl=random.uniform(19,1)#also 1,19
# print(random_fl)
# #use in love calc
# love_score=random.randint(1,100)
# print(f"love score is {love_score}")
# #OWN MODULES

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