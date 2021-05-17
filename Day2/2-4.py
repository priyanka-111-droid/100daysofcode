#Day 2:Project-Tip calculator

print("Welcome to the tip calculator")

bill=input("What was the total bill?")

perc=input("What percentage tip would you like to give?10,12,or 15?")

ppl=input("How many people to split the bill?")

#everything into float but take ppl as int
total=(float(bill)+(float(perc)/100)*float(bill))/int(ppl)


#rounding by f string using round will give 33.6 not 33.60

print(f"Each person should pay:${round(total,3)}") 

#if we need 33.60,we need rounding AND formatting
#rounding and formatting using f string ONLY...
print(f"Each person should pay :${total:.2f}")


#rounding and formatting using format and f string
amt="{:.2f}".format(total)
print(f"Each person should pay: ${amt}")
