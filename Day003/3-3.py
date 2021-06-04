'''
Leap year:
Find out if year entered is leap year:
Check if it is divisible by 4 
1)If yes,
-if it is divisible by 100 but not divisible by 400 ,then it is not leap year
-if it is divisible by 100 and divisible by 400,then it is leap year
2)If no,
it is not a leap year
'''

year=int(input("Which year you wish to check?"))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")
