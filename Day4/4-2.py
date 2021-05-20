#LIST DATA STRUCTURE
#fruits=[item1,item2]
#print(fruits[0]) list offsets can be positive or negative in python
#fruits.append("Cherry")
#fruits.extend(["Papaya","Pineapple"])
#fruits.remove("Cherry")
#fruits.pop([1]) pop and return it

#########<<<<PROGRAM>>>>##########
'''Banker Roulette-Who will pay the bill? give names as input and pick random name
'''
import random
input_str=input("give me all names comma separated")
names=input_str.split(',')  #is now a list
n=random.randint(0,(len(names)-1))
print(f"{names[n]} has to pay the bill today.")

#Better way:use random.choice() to pick an item from list or sequence
print(f"{random.choice(names)} has to pay the bill today.")

#Mistakes:
#Try to make input user generated instead of predefined lists
#don't use for loops unnecessarily here


