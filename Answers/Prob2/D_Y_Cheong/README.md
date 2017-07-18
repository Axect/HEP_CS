# Yonsei HEP-COSMO Coding Study
## Problem 2.
### Dhong Yeon Cheong

1. Roll a Dice!

This code uses a random function that chooses a random number from 1 to 6. It is expressed as 
```Python
from random import randrange
def Diceroll():
    Droll = randrange(1,7)
    if Droll == 1:
        return "1"
    if Droll == 2:
        return "2"
    if Droll == 3:
        return "3"
    if Droll == 4:
        return "4"
    if Droll == 5:
        return "5"
    if Droll == 6:
        return "6"
```
Thus this part of the program acts like a physical dice.
<br>
Now, we need to determine the probability for 5 to occur in 1 million trials, or basically any large number. The following code achieves the task

```Python
def quincunx():
    count = 0
    n = 10000000
    for i in range(n):
        if Diceroll() == "5":
            count +=1
    prob = (count)/(n)
    print("The prob for the quincunx is",prob)
```
The result for one trial gave a result of "The prob for the quincunx is 0.1666097". This is close to the theoretical probability for an unbiased dice, where each side has a 0.16667 probability.

2. Sort a list.

A physics test table was given as following.
<br>

>| Name        | Score | 
>|-------------|-------:| 
>| Schrodinger | 64    | 
>| Einstein    | 90    | 
>| Feynman     | 98    | 
>| Neumann     | 100   | 
>| Dirac       | 92    | 
>| Bohr        | 90    | 
>| Fermi       | 91    | 
>| Heisenberg  | 72    | 
>| Pauli       | 88    | 
>| Newton      | 93    | 
>| Leibniz     | 93    | 
>| Planck      | 52    | 


I copyed this list into a csv file, and opened the csv file in python using the following code. And as the first line is considered as a header and was a serious burden processing it with the actual data, I removed it by removing the first element of the list.

```Python
import csv
import operator as op
import math
import matplotlib.pyplot as plt
def In() : 
    reader = csv.reader(open("Phytest.csv"), delimiter = ",")
    my_list = list(reader)
    return my_list

def Remove():
    ilist = In()
    del ilist[0]
    return ilist
```
The default setting of the imported csv data is a string, which makes processing a real pain. Thus, I changed the 2nd column in the list in list into a float datatype. To achieve this, I split the list in list into two separate lists, and changed the datatype.
```Python
def slist():
    dlist = Remove()
    iget0 = op.itemgetter(0)
    
    slist = list(map(iget0, dlist))
    return slist

def flist():
    flist = Remove()
    iget1 = op.itemgetter(1)

    flist = list(map(iget1, flist))
    return flist
    
def convert():
    nlist = flist()
    
    clist = list(map(float, nlist))

    return clist
```
Before merging back into a list in list, I proceeded calculating the mean and the standard deviation of the score. The code executing this is 
```Python
def mean():
    x = convert()
    mean = sum(x)/(len(x))
    
    return mean

def std():
    clist = convert()
    m = mean()
    ss = sum((x-m)**2 for x in clist)
    std = math.sqrt(ss/len(clist))

    return std
```
Now that I finished calculating the numerical data of the score, I merged these two separate lists back, and sorted the merged list based on the criteria of column 2. I used the itemgetter from operator, and as we need to sort in reverse order, I set the mode as "reverse = True"
```Python
def merge():
    l1 = slist()
    l2 = convert()

    lmerge = list(list(l) for l in zip(l1, l2))
    
    return lmerge

def sort():
    la = merge()

    sorlist = sorted(la, key = op.itemgetter(1), reverse=True)

    return sorlist
```
Now from here, I really screwed up my whole algorithm. I attempted to rank the scores by keeping the sorted merged list, but I failed to achieve the result using that method. So, I split the list again, took the score column, sorted in normal order, and reversed it. 
```Python
def split():
    split = list(map(op.itemgetter(1), sort()))
    return split

def rank(a):
    n = len(a)
    ivec = sorted(range(n),key=a.__getitem__)
    svec= [a[rank] for rank in ivec]
    sumrank = 0
    dupcount = 0
    newarray = [0]*n
    
    for i in range(n):
        sumrank += i
        dupcount += 1
        if i == n-1 or svec[i] != svec[i+1]:
            for j in range(i-dupcount+1, i+1):
                newarray[ivec[j]] = i+1

            sumrank = 0
            dupcount = 0

    return newarray

def reverse():
    rarray = rank(split())
    n2 = len(rarray)
    

    return [n2-x+1 for x in rarray]
```
Finally, I merged everything into a list, and exported the list as a csv file. Then I used this csv file to plot the distribution of the score and rank.
```Python
def Finalmerge():
    sflist1 = list(map(op.itemgetter(0),sort()))
    sflist2 = list(map(op.itemgetter(1),sort()))
    rlist = reverse()

    merge = list(list(l) for l in zip(sflist1, sflist2, rlist))


    return merge

def Nowdoit():
    print("Mean is ",mean())
    print("STD is ", std())

    with open('Sorted Phytest.csv', "w", newline="") as f :
        writer = csv.writer(f)
        writer.writerows(Finalmerge())

Nowdoit()

with open('Sorted Phytest.csv','r') as f:
    fopen = list(csv.reader(f))

rank = [i[2] for i in fopen]
score = [i[1] for i in fopen]

plt.title("Score of Exam")
plt.plot(rank, score, label = 'score distribution')
plt.legend(loc='upper left')
plt.xlabel('rank')
plt.ylabel('score')
plt.savefig("Sorted Phytest.png")
```
The total code will then be, with a staggering 128 lines,
```Python
import csv
import operator as op
import math
import matplotlib.pyplot as plt
def In() : 
    reader = csv.reader(open("Phytest.csv"), delimiter = ",")
    my_list = list(reader)
    return my_list

def Remove():
    ilist = In()
    del ilist[0]
    return ilist

def slist():
    dlist = Remove()
    iget0 = op.itemgetter(0)
    
    slist = list(map(iget0, dlist))
    return slist

def flist():
    flist = Remove()
    iget1 = op.itemgetter(1)

    flist = list(map(iget1, flist))
    return flist
    
def convert():
    nlist = flist()
    
    clist = list(map(float, nlist))

    return clist

def mean():
    x = convert()
    mean = sum(x)/(len(x))
    
    return mean

def std():
    clist = convert()
    m = mean()
    ss = sum((x-m)**2 for x in clist)
    std = math.sqrt(ss/len(clist))

    return std

def merge():
    l1 = slist()
    l2 = convert()

    lmerge = list(list(l) for l in zip(l1, l2))
    
    return lmerge

def sort():
    la = merge()

    sorlist = sorted(la, key = op.itemgetter(1), reverse=True)

    return sorlist

def split():
    split = list(map(op.itemgetter(1), sort()))
    return split

def rank(a):
    n = len(a)
    ivec = sorted(range(n),key=a.__getitem__)
    svec= [a[rank] for rank in ivec]
    sumrank = 0
    dupcount = 0
    newarray = [0]*n
    
    for i in range(n):
        sumrank += i
        dupcount += 1
        if i == n-1 or svec[i] != svec[i+1]:
            for j in range(i-dupcount+1, i+1):
                newarray[ivec[j]] = i+1

            sumrank = 0
            dupcount = 0

    return newarray

def reverse():
    rarray = rank(split())
    n2 = len(rarray)
    

    return [n2-x+1 for x in rarray]


def Finalmerge():
    sflist1 = list(map(op.itemgetter(0),sort()))
    sflist2 = list(map(op.itemgetter(1),sort()))
    rlist = reverse()

    merge = list(list(l) for l in zip(sflist1, sflist2, rlist))


    return merge

def Nowdoit():
    print("Mean is ",mean())
    print("STD is ", std())

    with open('Sorted Phytest.csv', "w", newline="") as f :
        writer = csv.writer(f)
        writer.writerows(Finalmerge())

Nowdoit()

with open('Sorted Phytest.csv','r') as f:
    fopen = list(csv.reader(f))

rank = [i[2] for i in fopen]
score = [i[1] for i in fopen]

plt.title("Score of Exam")
plt.plot(rank, score, label = 'score distribution')
plt.legend(loc='upper left')
plt.xlabel('rank')
plt.ylabel('score')
plt.savefig("Sorted Phytest.png")
```

3. Rock Scissors Paper!

This problem typically states to generate a random program that can do Rock, Scissors, and Paper. 
<br>
My code is consisted of two parts. The first part does the computer role. First we generate a random list from 0 to 2, and assigned these numbers each to "Rock", "Scissors", and "Paper"
```Python
from random import randrange
def computer():
    comresult = randrange(0,2)
    if comresult == 0:
        return "Rock"
    if comresult == 1:
        return "Scissors"
    if comresult == 2:
        return "Paper"
```
The second part does the human role. It takes an input of strings among the options "Rock", "Scissors", and "Paper", and then compares with the computer result and returns the appropriate match result according to the Official RSP rules. Finally, as every RSP game needs to taunt the loser, I outputed a sentence that will highly irritate the player.
```Python
def fight():
    huminput = input("Rock, Scissors, Paper! ")
    computer()
    if huminput == computer():
        print("Tie! try again")
    elif huminput == "Rock":
        if computer() == "Paper":
            print("HAHA You lose!")
        else :
            print("Meh You win")
    
    elif huminput == "Scissors":
        if computer() == "Rock":
            print("HAHA You lose!")
        else :
            print("Meh You win")
    
    elif huminput == "Paper":
        if computer() == "Scissors":
            print("HAHA You lose")
        else :
            print("Meh You win")

fight()
```
4. Calendar generator

Fighting the temptation to just use the simple, precise 'calendar' module, I generated a code to generate a calendar.

First I assigned a list that corresponds to the number of days in each month. Then, I defined a function that determines the leap year of the inputed year.
```Python
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
```
Then, I inputed the data of a specific date, assigned it to a list, then set each element to the year, month, and day in the preceding order. 
```Python
user_input = input("Enter year.month.date ")
date = list(map(int, user_input.split('.')))

year = date[0]
month = date[1]
day = date[2]
```
Now we need to define the number of days in a year. To achieve this, I defined a function as
```Python
def day_of_year(j):
    if leap_determine(j)==True:
        calendar[1] = 29
        dyear1 = sum(calendar[i] for i in range(12))
        
    else: 
        calendar[1] = 28
        dyear1 = sum(calendar[i] for i in range(12))
        
    return dyear1
``` 
The if statement changes the number of days in February according to the leap year rule.

Then, I summed up the total days of the imported date using
```Python
dyear = sum(day_of_year(j) for j in range(1, year))
dmonth = sum(calendar[i] for i in range(month-1))
dday = day

Total_day = dyear + dmonth + dday
```
Now, we need to determine the day of the imported date. As AD 0001.1.1 is a Monday, I used the following code to determine the day of the date.
```Python
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
```
So, the total code will be
```Python
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
```


