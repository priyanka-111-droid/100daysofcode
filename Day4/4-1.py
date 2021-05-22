#RANDOMIZATION

#pseudo random number generator(see Khan academy)uses Mersenne twister but in python we can implement this using random module easily
# import random
# random_integer = random.randint(1,10)  #return integer from 1 to 10 that is stored in random_integer
# random_float=random.random()     #returns float from 0 to 1 stored in random_float
# random_fl=random.uniform(19,1)   #can also be (1,19),This returns random float stored in random_fl
# print(random_fl)
# #can be used in love calc done in day 3
# love_score=random.randint(1,100)

# #USING OUR OWN MODULES
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
