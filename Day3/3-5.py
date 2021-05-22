#logical operators (or ,and ,not)
#####<<<<PROGRAM>>>#######
'''love calculator
1.Combine your name and crush's name
2.Take the word "TRUE" and count number of times each letter in "TRUE" occurs in your combined name
3.Take the word "LOVE" and count number of times each letter in "LOVE" occurs in your combined name
4.Now combine (NOT ADD) values obtained in steps 2 and 3 into a two digit number
5.If answer is <=10 or >=90,you are perfect for each other
6.If answer is >=40 and <=50,you are alright for each other
7.Else just print the answer
'''

print("Welcome to the love calculator!")
name1=input("What is your name?")
name2=input("What is your name?")
lis1=['t','r','u','e']
lis2=['l','o','v','e']

count1=count2=0;
#combining both your name and crush's name
fullname=name1.lower()+name2.lower()
#using count() function
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



