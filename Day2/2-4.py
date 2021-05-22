#Day 2:Project-Tip calculator
'''
Input bill,percentage tip(10,12,15) and people to split the bill
Then round off and format up to 2 decimal places
'''

print("Welcome to the tip calculator")

bill=input("What was the total bill?")

perc=input("What percentage tip would you like to give?10,12,or 15?")

ppl=input("How many people to split the bill?")

#everything into float but take number of ppl as int
#total is bill + percentage of bill and this is divided among ppl
total=(float(bill)+(float(perc)/100)*float(bill))/int(ppl)


#rounding by f string using round will give 33.6 NOT 33.60
print(f"Each person should pay:${round(total,2)}") 

#if we need 33.60,we need rounding AND formatting
#rounding and formatting using ONLY f string ...
print(f"Each person should pay :${total:.2f}")


#rounding and formatting using format and f string
amt="{:.2f}".format(total)
print(f"Each person should pay: ${amt}")
