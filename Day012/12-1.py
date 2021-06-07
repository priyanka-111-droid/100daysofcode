
#SCOPE:
enemies=1
def increase_enemies():
    enemies=2
    print(f"Enemies inside function:{enemies}") #2

increase_enemies()
print(f"Enemies outside function:{enemies}")  #1



#LOCAL SCOPE:
def drink_portion():
    portion_strength=2
    print(portion_strength)

drink_portion() #2
#print(portion_strength) gives error 
#portion_strength cannot be accessed outside drink_portion() function since it has local scope

#What do we mean by local scope???
#When you create a new variable or new function,inside another function,you can 
#only use it when you are inside that function and hence we say it has local scope



#GLOBAL SCOPE:
player_health=10

def drink_fruitjuice():
    juice_strength=2
    print(player_health)

drink_fruitjuice() #10
print(player_health) #10

#Since player_health is created outside drink_fruitjuice(),it can be accessed outside function too
#Hence we say it has global scope.

