#leap year exercise
#find out if given year is leap year

year=int(input("Which year you wish to check?"))

if(year%4==0):
    if(year%100==0 and year%400!=0):
        print("Not leap year")
    elif(year %100==0 and year%400==0):
        print("Leap year")
else:
    print("Not leap year")
