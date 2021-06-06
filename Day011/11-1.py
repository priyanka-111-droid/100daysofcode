
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def dealer():

    dealer_card=random.choice(cards)
    return(dealer_card)

def user():
    user_cards=[]
    for i  in range(2):
        user_cards.append(random.choice(cards))

    return user_cards 
    
def dealer_finalhand():
    hidden=random.choice(cards)
    return hidden

def compare(user_cards,all_dealer_cards):
    if(sum(user_cards)==21):
        print("You win with a blackjack!")
    elif(sum(all_dealer_cards)==21):
        print("You loose,opponent wins with blackjack...")
    elif(sum(all_dealer_cards)>21):
        print("Opponent went over,you win!")
    elif(sum(user_cards)>21):
        print("You went over,you loose..") 
    else:
        if(sum(all_dealer_cards)>sum(user_cards)):
            print("You loose")
        else:
            print("You win!")

def blackjack():
    all_dealer_cards=[]
    user_cards=user()
    print(f"Your cards are {user_cards},current score is {sum(user_cards)}")
    dealer_card=dealer()
    all_dealer_cards.append(dealer_card)
    print(f"Computer's first card:{all_dealer_cards}")
    terminate=False
    while not terminate:
        if(input("Type 'y' to get another card,type 'n' to pass:")=='n'):
            print(f"Your final hand:{user_cards},final score:{sum(user_cards)}")
            hidden=dealer_finalhand()
            all_dealer_cards.append(hidden)
            while(sum(all_dealer_cards)<17):
                till_seventeen=dealer_finalhand()
                all_dealer_cards.append(till_seventeen)
            print(f"Computer final hand:{all_dealer_cards},final score:{sum(all_dealer_cards)}")
            terminate=True
        else:
            user_again=dealer_finalhand()
            user_cards.append(user_again)
            print(f"Your cards are {user_cards},current score is {sum(user_cards)}")
            print(f"Computer's first card:{all_dealer_cards}")
            if(sum(user_cards))>21:
                print(f"Your final hand:{user_cards},final score:{sum(user_cards)}")
                hidden=dealer_finalhand()
                all_dealer_cards.append(hidden)
                print(f"Computer final hand:{all_dealer_cards},final score:{sum(all_dealer_cards)}")
                terminate=True

    compare(user_cards,all_dealer_cards)
    
        
should_end=False
while not should_end:
    if(input("Do you wish to play blackjack?Press y if yes else n :")=="y"):
        print(logo)
        blackjack()
    else:
        print("Thanks for playing,goodbye...")
        should_end=True  

    




    






