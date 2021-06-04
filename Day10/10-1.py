def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return False
  else:
    return False

def days_in_month(year_input,month_input):
  """
  This is called a docstring,used to describe what this function does:
  Take the year and month as input and check if year is leap year or not and accordingly return 
  number of days in that month.
  """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  #Remember that month_days is a List and Lists in Python start at position 0.
  #So the number of days in January is month_days[0]
  
  if is_leap(year_input):  # if it is leap year
      if month_input==2:  #2 meaning February
          return (month_days[month_input-1]+1)  #28+1=29 days
  
  return month_days[month_input-1] #eg if month_input is 4(April),return month_days[3] which is April
      


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
