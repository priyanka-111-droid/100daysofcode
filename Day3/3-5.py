#logical operators (or ,and ,not)

#####<<<<PROGRAM>>>#######
'''love calculator'''

print("Welcome to the love calculator!")
name1=input("What is your name?")
name2=input("What is your name?")
lis1=['t','r','u','e']
lis2=['l','o','v','e']

count1=count2=0;
#using count() function
fullname=name1.lower()+name2.lower()
for x in lis1:
    count1+=fullname.count(x)
for y in lis2:
    count2+=fullname.count(y)


ans=0
#convert to string and concat
ans=str(count1)+str(count2)
#convert to int to compare
check=int(ans)

if(check<=10 or check>=90):
    print(f"your score is {check} and you go together like coke and mentos")
elif(check>=40 and check<=50):
    print(f"Your score is {check},you are alright together")
else:
    print(f"Your score is {check}")



