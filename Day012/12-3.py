#MODIFYING VARIABLES WITH GLOBAL SCOPE:

# enemies=1 #variable enemies with global scope
# def increase_enemies():
#     #this function creates local scope
#     enemies=2
#     #we are creating NEW variable enemies completely different from global enemies
#     #We are NOT changing global enemies
#     print(f"enemies inside function:{enemies}")    #2

# increase_enemies()
# print(f"enemies outside function:{enemies}")       #1

#######################################################################################
# # bad idea to call local and global variable same name
# # But what if I wished to modify global variable enemies inside local scope?

# enemies=1
# def increase_enemies():
#     #this function creates local scope
#     global enemies #now we can accesss global enemies inside local scope
#     print(f"enemies inside function:{enemies}") #1  
#     enemies+=1

# increase_enemies()
# #We have changed global enemies  
# print(f"enemies outside function:{enemies}")  #2      

#######################################################################################
#But avoid modifying global scope in function with local scope,causes many bugs
#But how do you achieve above result without modifying global scope?

enemies=1
def increase_enemies():
    print(f"enemies inside function:{enemies}")   #1
    return enemies+1  

enemies=increase_enemies() #save result to global variable enemies
print(f"enemies outside function:{enemies}")      #2

#Now we can use above function increase_enemies() anywhere in our code,no problems about bugs in code