#There is no block scope in python
# To remember:
# If we create a variable within function,then its ONLY available
# inside function.But variable inside if block,for loop or while loop
# or anything with indentation and colon,then that DOES NOT count as 
# creating a separate local scope.


#############<<<EXAMPLE 1>>>>>##################
# game_level=3
# enemies=["Skeleton","Zombie","Aliens"]
# if game_level<5:
#     new_enemy=enemies[0]
# #new_enemy created inside if block

# print(new_enemy)
# #outside if block new_enemy can be printed
# #Above print statement is valid 

################<<<<EXAMPLE 2>>>>>###############
game_level=3
def create_enemy():
    enemies=["Skeleton","Zombie","Aliens"]
    if game_level<5:
        new_enemy=enemies[0]
#new_enemy created inside if block

#print(new_enemy) 
#now this line gives error
#now new_enemy available only inside function


#In python,if ,else ,while,for with indents and colon, don't count as 
#creating a local scope

    print(new_enemy)

#to print new_enemy we need to be within boundary of create_enemy()
#So indent the line print(new_enemy)

