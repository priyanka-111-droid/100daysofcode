
import random
from art import logo

cards=["A","2","3","4","5","6","7","8","9","K","Q","J"]
'''
Real cards have been used here
'''
def total(sample):
    s=0
    for x in sample:
        if(x=="A"):
            s=s+11
        elif(x=="K" or x=="Q" or x=="J"):
            s=s+10
        else:
            s=s+int(x)

    if(s>21 and "A" in sample):
         s=s-10    

    return(s)

def dealer():
    '''computer is the dealer'''
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



def natural(user_cards,all_dealer_cards,bank,bet):
    '''
    natural is when user has 21 in first 2 cards itself(Ace and K/Q/J)
    '''
    if(total(user_cards)==21):
        hidden=dealer_finalhand()
        all_dealer_cards.append(hidden)
        
        if(total(all_dealer_cards)==21):
            print(f"Your final hand:{user_cards},final score:{total(user_cards)}")
            print(f"Computer final hand:{all_dealer_cards},final score:{total(all_dealer_cards)}")
            print("Its a tie..you and dealer have blackjack,you get back your bet..")
            bank= bank + bet 
            print(f"Your bank now has:${bank}")
            return bank
        else:
            print(f"Your final hand:{user_cards},final score:{total(user_cards)}")
            print(f"Computer final hand:{all_dealer_cards},final score:{total(all_dealer_cards)}")
            print("Congrats,you won a natural 21!")
            bank=bank+bet+1.5*bet 
            print(f"Your bank now has:${bank}")
            return bank
    else:
        return -1



def compare(user_cards,all_dealer_cards,bank,bet):
    if(total(all_dealer_cards)==total(user_cards)):
        print("Its a tie..you get back your bet..")
        bank=bank+bet 
    elif(total(user_cards)==21):
        print("You win with a blackjack!")
        bank=bank+bet+1.5*bet
    elif(total(all_dealer_cards)==21):
        print("You loose,opponent wins with blackjack...")
        bank=bank-1.5*bet 
    elif(total(user_cards)>21):
        print("You went over,you loose..")
    elif(total(all_dealer_cards)>21):
        print("Opponent went over,you win!")
        bank=bank+bet*2
    else:
        if(total(all_dealer_cards)>total(user_cards)):
            print("You loose")
        else:
            print("You win!")
            bank=bank+bet*2 

    if(bank>=0):
        print(f"Your bank now has:${bank}")
    elif(bank<0):
        print(f"Your bank is short of ${abs(bank)}")
        print("Please recharge your bank")

    return bank







def blackjack(bank,bet):
    user_cards=user()
    all_dealer_cards=[]
    print(f"Your cards are {user_cards},current score is {total(user_cards)}")
    dealer_card=dealer()
    all_dealer_cards.append(dealer_card)
    print(f"Computer's first card:{all_dealer_cards}")
    value=natural(user_cards,all_dealer_cards,bank,bet)
    if (value==-1):
        terminate=False
        while not terminate:
            if(input("Type 'y' to get another card,type 'n' to pass:")=='n'):
                print(f"Your final hand:{user_cards},final score:{total(user_cards)}")
                hidden=dealer_finalhand()
                all_dealer_cards.append(hidden)
                while(total(all_dealer_cards)<17):
                    till_seventeen=dealer_finalhand()
                    all_dealer_cards.append(till_seventeen)
                print(f"Computer final hand:{all_dealer_cards},final score:{total(all_dealer_cards)}")
                terminate=True
            else:
                user_again=dealer_finalhand()
                user_cards.append(user_again)
                print(f"Your cards are {user_cards},current score is {total(user_cards)}")
                print(f"Computer's first card:{all_dealer_cards}")

                if(total(user_cards))>21:
                    hidden=dealer_finalhand()
                    all_dealer_cards.append(hidden)
                    while(total(all_dealer_cards)<17):
                        till_seventeen=dealer_finalhand()
                        all_dealer_cards.append(till_seventeen)

                    print(f"Your final hand:{user_cards},final score:{total(user_cards)}")
                    print(f"Computer final hand:{all_dealer_cards},final score:{total(all_dealer_cards)}")
                    terminate=True

        bank1=compare(user_cards,all_dealer_cards,bank,bet)
    else:
        bank1=value 


    return bank1



def welcome():
    print(logo)
    print("Welcome to 21 casino!!")
    # By default,every time we start game our bank is credited with $100,
    # User can input bets 
    # In case after playing once ,if this money finishes,there is an option to recharge bank 

    bank=100 
    should_end=False 
    while not should_end:
        if(bank>0):
            print(f"Your bank  has :${bank}")
            bet=int(input("How much would you like to bet?"))
            while(bet>bank):
                bet=int(input("Please bet amount less than or equal to your bank amount :"))

            bank=bank-bet 
            bank2=blackjack(bank,bet) 
            ans=input("\npress y to continue,n to end game :\n")
            if(ans=='n'):
                print("Thank you for playing!")
                should_end=True
            elif(ans=='y'):
                bank=bank2 

        else:
            answer=input("Sorry your bank has no cash..Press y if you wish to recharge or n to quit :")
            if(answer=='n'):
                print("Thank you for playing!")
                should_end=True
            else:
                recharge=int(input("Enter your new bank amount now :"))
                bank=recharge 


          
welcome()

