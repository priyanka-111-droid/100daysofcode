#LIST DATA STRUCTURE
#fruits=["apple","mango"]
#list offsets/index can be positive or negative in python
#print(fruits[0]) #Here 0 is the offset/index and apple is printed
#fruits.append("Cherry") will attach "Cherry"to end of list
#fruits.extend(["Papaya","Pineapple"]) to add another list to end of fruits list
#fruits.remove("Cherry") 
#fruits.pop([1]) pop and returns mango

#########<<<<PROGRAM>>>>##########
'''Banker Roulette-Who will pay the bill? Give names as input and pick random name'''

import random
input_str=input("give me all names comma separated")
names=input_str.split(',')  #is now a list
n=random.randint(0,(len(names)-1)) #pick random integer
print(f"{names[n]} has to pay the bill today.")  #print name at that index in names list

#Better way:use random.choice() to pick an item from list or sequence
print(f"{random.choice(names)} has to pay the bill today.")

#Mistakes:
#Try to make input user generated instead of predefined lists
#don't use for loops unnecessarily here


