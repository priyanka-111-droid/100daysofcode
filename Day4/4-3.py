#IndexOutOfRange error
#Lets say we have a list l with number of elements n
#index of left most element is 0 and index of last element is n-1 
#If you try to print element at index [n] you get the error as last element in the list was present at index n-1.
#NESTED LISTS
# dirty_dozen=["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]
# fruits=["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
# vegetables=["Spinach","Kale","Celery","Potatoes"]
# nested_list=[fruits,vegetables]

########<<<<<PROGRAM>>>#########
'''
Treasure Map:
given a 3x3 grid ,
input column number,row number and update that coordinate with "X" to denote presence of treasure
'''
row1=["O","O","O"]
row2=["O","O","O"]
row3=["O","O","O"]
map=[row1,row2,row3]   #nested list,not related to map() of python..
print(f"{row1}\n{row2}\n{row3}") 

position=input("Where do you wish to put the treasure? ") #taking input as string
# let's say 23-column 2 and row 3

vertical=int(position[1])-1   #2(index)
horizontal=int(position[0])-1 #1(index)

map[vertical][horizontal]="X" #go down vertically to row3(index 2) and then to column2(index 1)
print(f"{row1}\n{row2}\n{row3}")

