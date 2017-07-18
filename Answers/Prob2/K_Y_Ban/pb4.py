# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:53:50 2017

@author: Bany
"""

y = int(input("Please input year = "))  # input year
m = int(input("Please input month = "))  # input month
d = int(input("Please input day = "))  # input date

def moon(y):  # 윤년의 경우 (4년마다 돌아오지만 100년마다는 아니고 400년마다는 윤년)
    if(y%400==0):  
        return True
    elif(y%100==0):
        return False
    elif(y%4==0):
        return True
    else:
        return False

n = int(input("Please input days = "))  # how many days after

eod=[31,28,31,30,31,30,31,31,30,31,30,31]  

##################### calculate day & month #####################
# ex) if 17.06.09, n=100 -> d=09+100=109, m=6 -> d=109-30=79, m=7 -> d=79-31=48, m=8 -> d=48-31=17, m=9 -> end
d = d + n   # after n days, total day
while(d>31):  
    d = d - eod[m-1] 
    if(moon(y)):  # if 윤년 not -28, but -29
        if(m==2):
            d = d - 1
        else:
            d = d
    else:
        d = d
    m = m + 1
    ##################### modify special case of month #####################
    # ex) if 17.10.10, n=100 -> d=10+100=110, m=10 -> d=110-31=79, m=11 -> d=79-30=49, m=12 -> d=49-31=18, m=13
    while(m>12):# the case m is larger than 12. we need month 1 to 12
        m = m - 12
        y = y + 1  # go to next year if m>12
        
if(moon(y)):  # the case if 윤년, m=2, d=30 or 31
    if(m==2):
        if(d==30):
            m = m + 1
            d = d - 29
        elif(d==31):
            m = m + 1
            d = d - 29            
        else:  # 아니면 그냥 지나가라
            m = m
            d = d        

    
print('%d %d %d'%(y,m,d))


# 코드 수정했습니다! 혹시 이해안되는 부분이나 이상한 점 있다면 ban94gy@naver.com으로 문의주세용! :>


