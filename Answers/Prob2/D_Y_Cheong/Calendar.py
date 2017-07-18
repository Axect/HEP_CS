calendar = [31,28,31,30,31,30,31,31,30,31,30,31]

def leap_determine(year):
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

user_input = input("Enter year.month.date ")
date = list(map(int, user_input.split('.')))

year = date[0]
month = date[1]
day = date[2]


def day_of_year(j):
    if leap_determine(j)==True:
        calendar[1] = 29
        dyear1 = sum(calendar[i] for i in range(12))
        
    else: 
        calendar[1] = 28
        dyear1 = sum(calendar[i] for i in range(12))
        
    return dyear1


dyear = sum(day_of_year(j) for j in range(1, year))
dmonth = sum(calendar[i] for i in range(month-1))
dday = day

Total_day = dyear + dmonth + dday-1

day_find = (Total_day) % 7

def Day_finding(day_find):  
    if day_find == 0:
        return "Sun"
    elif day_find == 1:
        return "Mon"
    elif day_find == 2:
        return "Tue"
    elif day_find == 3:
        return "Wed"
    elif day_find == 4:
        return "Thu"
    elif day_find == 5:
        return "Fri"
    elif day_find == 6:
        return "Sat"

print("It is "+str(Total_day)+"days AD, and it is a "+Day_finding(day_find))

Total_day_100 = Total_day + 100
day_find_mod = (Total_day_100)%7


print("It is a "+Day_finding(day_find_mod)+" after 100 days from the inputed date")





    


