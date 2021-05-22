#LIST DATA STRUCTURE
#data structure is a way to organize and store data.Examples in python are lists,tuples,sets,dictionaries
#Now let us see lists
#fruits=["apple","mango","grapes"] 
#list offsets/index can be positive or negative in python
#example list fruits has 3 elements and index of leftmost element is 0 and rightmost is 2(number of elements - 1)
#But we can also start from rightmost element of the list so index of rightmost element is -1 and then -2 and so on
#print(fruits[0]) #Here 0 is the offset/index and apple is printed
#print(fruits[-1]) #Here grapes is printed
#fruits.append("Cherry") # append will attach "Cherry"to end of list 
#fruits.extend(["Papaya","Pineapple"])  # extend adds another list to end of fruits list
#fruits.remove("Cherry") #remove deletes the item Cherry but DOES NOT return deleted value so it cannot be stored in another variable
#popped_value=fruits.pop([1]) #pop removes element at index 1(mango) and returns it so it can be stored in popped_value

#########<<<<PROGRAM>>>>##########
'''Banker Roulette-Who will pay the bill? Give names as input and pick random name'''

import random
input_str=input("give me all names comma separated")
names=input_str.split(',')  #is now a list
n=random.randint(0,(len(names)-1)) #pick random integer
print(f"{names[n]} has to pay the bill today.")  #print name at that index in names list

#Better way:use random.choice() to pick an item from list or sequence
print(f"{random.choice(names)} has to pay the bill today.")

#Mistake:
#Don't need to use for loop to go through list here.

