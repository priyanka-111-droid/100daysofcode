import datetime as dt

# module datetime has class datetime and this is confusing hence rename module to dt
# datetime.datetime
now=dt.datetime.now()
# print(now)

year=now.year
if year==2021:
   print("Wear a mask") 

month=now.month

day_of_week=now.weekday()
print(day_of_week)
#0 :Monday
#1 :Tuesday and so on

date_of_birth=dt.datetime(year=1997,month=6,day=10,hour=4)
print(date_of_birth)





