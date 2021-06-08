
# #Step 3: Play Computer

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# 1.Input year by year eg.check for 1990
# 2.Look at each line of code and see what it will evaluate
# 3.Now check for 1994
# 4.Error occurs when you type in 1994

###<<<SOLUTION>>>###



year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994: 
  print("You are a millenial.")
elif year >=1994:
  print("You are a Gen Z.")

#1.Now we realize neither if nor else blocks catch 1994
#2.you can write <=1994 in if block or >=1994 in else block
