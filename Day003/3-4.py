#multiple if statements
#in if-elif-else if first condition is true,we execute that and skip remaining conditions
#But what if we need to check multiple conditions even if previous conditions were true
#here we use multiple if statements
####<<<PROGRAM>>>>####
'''
Pizza order exercise:
Input size(S,M,L),if they want pepperoni and if they want extra cheese
Work out the final bill based on following prices:
Small pizza:$15
Medium Pizza:$20
Large pizza:$25
pepperoni for small pizza: +$2
Pepperoni for medium or large pizza: +$3
extra cheese for any size pizza: +$1
'''
print("welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want?")
add_pep=input("Do you want pepperoni?Y or N")
extra_cheese=input("Do you want extra cheese?Y or N")

bill=0;
#for size we use if-elif because if one condition is true,we don't need to check remaining conditions
if(size=="S"):
    bill+=15
elif(size=='M'):
    bill+=20
else:
    bill+=25
#but here for pepperoni and extra cheese,we use if because we always want to ensure we check these conditions
if add_pep =="Y":
    if(size=="S"):
        bill+=2
    else:
        bill+=3
if(extra_cheese =="Y"):
    bill+=1

print(f"Your final bill is ${bill}")



