#Project:treasure island
#diagram taken from ascii.co.uk/art
#for same feedback like gameover ,use if else
#for diff feedback like you got burnt by fire or killed by beasts,
#use if elif else
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
'''
)
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure")
dir=input("You are at a crossroads,which direction do you want to go in?left or right\n")


if(dir=="right"):
    print("Game over")
    
elif(dir =="left"):
    action=input("You want to swim or wait?\n")
    if(action=="swim"):
        print("Game over")
        
    elif(action=="wait"):
        door=input("Which door do you choose?red,blue or yellow\n")
        if(door=="blue" or door=="red"):
            print("Game over")
            
        elif(door=="yellow"):
            print("Congrats...you win!!!")
            
        else:
            print("Choose red,blue or yellow")
            
    else:
        print("Choose action as swim or wait only")
        
else:
    print("Sorry choose left or right only")

