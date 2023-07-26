#https://projecteuler.net/problem=19

#year has 365 days, leap years has 366 days.

days_normal_year=[31,28,31,30,31,30,31,31,30,31,30,31] #how many days each month in a normal year has
days_leap_year = days_normal_year[:] # same as above for a leap year
days_leap_year[1] = 29
normal_year = [] #out of all 365 days which numbers are 1st days of the month
leap_year = [] #out of all 366 days which numbers are 1st days of the month
count = 0
sundays = [0 for i in range(101)] #we will go through all the years and put the # of 1st month sundays here
day = 0 #0 is monday, 1 is tuesday, .., 6 is sunday
year = 1901

for i in range(12):
    normal_year.append(sum(days_normal_year[:i+1]))
    leap_year.append(sum(days_normal_year[:i+1]))
    
    


while True:
    
    if year==2001: #finish
        break
    elif count != 3: #non-leap year
        temp = day
        while temp<normal_year[-1]+2:
            if temp in normal_year:
                sundays[year-1900]+=1
                temp+=7
            else:
                temp+=7
        year+=1
        count+=1
        day = (day + 365) % 7
        
    elif count == 3:
        temp = day
        while temp<leap_year[-1]+2:
            if temp in leap_year:
                sundays[year-1900]+=1
                temp+=7
            else:
                temp+=7
        year+=1
        count = 0
        day = (day+365)%7

print(sum(sundays))
