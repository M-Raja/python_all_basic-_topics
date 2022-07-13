
# date and time packages

#import package_name =(datetime) as dt--->alais name for datetime   datetime = dt
import datetime as dt 
# DATE

current_date = dt.date.today() #----> current date
print("current date",current_date) 

#var - new  package aslike name - dt  method (or) function - date()
new = dt.date(2021,10,25) #--->(year,month,day)

print(new)
print(new.year)
print(new.month)
print(new.day)

# TIME

a = dt.time(10,45,5,555505) #--->(hr:min:sec:micro_sec)
print(a)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)

current_time = dt.datetime.now() #------> show current time
print("current time:",current_time)

new = dt.datetime(2021,5,31,12,2,10) #---->(yr,mont,day,hr,min,sec)
print(new)
print(new.date())
print(new.time())
  

current = dt.datetime.now()
print(current)
s=current.strftime("%a %b %d %y")
print (s) 
# %a ---> day like monday,tuesday...
# %b --->month
# %d --->1,2,........,31 days
# %y --->year(2021,2020)