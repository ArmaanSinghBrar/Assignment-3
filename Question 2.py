#Finding the next date
day=int(input("Enter the day :"))
month=int(input("Enter the month :"))
year=int(input("Enter the year :"))

if year%400==0:
    leap_year= True
elif year%100==0:
    leap_year= False
elif year%4==0:
    leap_year= True
else:
    leap_year= False

if month in [1,3,5,7,8,10,12]:
    month_length=31

elif month==2 and leap_year==True:
    month_length=29
elif month==2 and leap_year==False:
    month_length=28
elif month>13:
    print('Please input the right month')
elif month in [4,6,9,11]:
    month_length=30

if day<month_length:
    day+=1
    print(f"The next date is {day}-{month}-{year}")
elif day==month_length and month<12:
    day=1
    month+=1
    print(f"The next date is {day}-{month}-{year}")
elif day>month_length or month>12:
    print("Error enter a valid date")
if day==month_length and month==12:
    day=1
    month=1
    year+=1
    print(f"The next date is {day}-{month}-{year}")
