#pizza order exercise
print("welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want?")
add_pep=input("Do you want pepperoni?Y or N")
extra_cheese=input("Do you want extra cheese?Y or N")

bill=0;
if(size=="Y"):
    bill+=15
elif(size=='M'):
    bill+=20
else:
    bill+=25

if add_pep =="Y":
    if(size=="S"):
        bill+=2
    else:
        bill+=3
if(extra_cheese =="Y"):
    bill+=1

print(f"Your final bill is ${bill}")



