#starting code already given 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,      #added this line 
            "coffee": 18,
            
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":5.0,   #I assumed machine already has $5 in it initially...
}

###################<<<<END OF STARTING CODE>>>>##########################

#to clear screen
from os import system,name

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



user_cash={
    "quarters":0.25,
    "dimes":0.10,
    "nickels":0.05,
    "pennies":0.01
}

def res():
    print("Current resource value:")
    for x in resources:
        print(f"{x}:\t{resources[x]}")

def money(user):
    print("Also,remember quarter is $0.25,dimes $0.10,nickels $0.05 and pennies $0.01\n\n") #not needed in code actually
    total=0
    for x in user_cash:
        coins=int(input(f"Enter number of {x} to be inserted:"))
        total=total+(user_cash[x]*coins)


    if(total<MENU[user]["cost"]):
        print("Sorry,that's not enough money. Money refunded.")
        return 0
       
    elif(total==MENU[user]["cost"]):
        #gets added to machine as profit(added to resources)
        resources["money"]+=total
        print(f"Here is your {user},enjoy it☕☕☕!\n")
        return 1
        
    else:
        #user has inserted too much money,give back change
        change=total-MENU[user]["cost"]
        print(f"Here is ${change:.2f} dollars in change.")
        print(f"Here is your {user},enjoy it☕☕☕!\n")
        return 1


   

def check_resources(user):
    coffee_ingre=MENU[user]["ingredients"]
    for x in coffee_ingre:
        quantity_needed=(coffee_ingre[x])
        if(quantity_needed>resources[x]):
            print(f"Sorry,there is not enough {x}")
            return 0
    
    return 1
            


def deduct_resources(user):
    if(check_resources(user)==1):    #resources are enough to make coffee required
        if(money(user)==1):          #user has successfully paid
            coffee_ingre=MENU[user]["ingredients"]
            for x in coffee_ingre:
                quantity_needed=(coffee_ingre[x])
                resources[x]=resources[x]-quantity_needed     #now reduce resources after making coffee


            
  


def order():
    #Prompt user

    letter=input("What would you like?Press e for espresso,l for latte and c for cappucino :")
    user=""
    if(letter=='e'):
        user="espresso"
    elif(letter=='l'):
        user="latte"
    else:
        user="cappuccino"

    deduct_resources(user)

    


#START OF PROGRAM---->
def welcome():
    # Displaying coffee and costs to user:
    print("\n\nWelcome to the coffee machine!!\n")
    terminate=False
    while not terminate:
        #formatted code using triple quoted string

        num=int(input('''
Press 1 to order coffee.
Press 2 to see report of resources available currently in machine
Press 3 to exit
Enter your choice:'''))
        if(num==1):
            clear()
            print("\t\t\tWelcome to the coffee machine!!")
            print("Coffee : \tCost")
            for x in MENU:
                coffee_cost=MENU[x]["cost"]       #to get costs of each coffee
                print(f"{x} : \t${coffee_cost}")   #displaying coffeename,\t for spacing and coffee cost for user

            order()
        elif(num==2):
            clear()
            res()
        else:
            print("Thank you,have a nice day!")
            terminate=True


welcome()












