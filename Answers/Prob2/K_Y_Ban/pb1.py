# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:45:26 2017

@author: Bany
"""

####################### problem 1 Rolling Dice ############################
import numpy as np
import random as rd

"""
#### by numpy ####
L1 = np.random.randint(1, 7, 10**6)
S1 = np.sum(L1)
        
        
print("Average is ", S1/(10**6))


#### by rand ####

def SUM():
    S = 0 # start
    for i in 10**6:
        num = rd.randrange(1,7)
        S = S + num            
            
return S

print("Average is ", S/(10**6))

"""

n = int(input("Please input n(for 1 to 6) = "))   # input 'n' 

L2=list(range(10**6))  # 10^6 times 

for i in range(10**6):  # 10^6 dice numbers
    L2[i] = rd.randrange(1,7)
    

count = 0 
for i in range(len(L2)): # Count how many times n comes out
    if(n==L2[i]):
          count = count+1
    elif(n>6):  # if n is not in 1 to 6 print error
        print("\nn must be in 1 to 6, plz retry") 
        break
    elif(n<1):  # if n is not in 1 to 6 print error
        print("\nn must be in 1 to 6, plz retry")         
        break

print("\nProbability is ", count/len(L2)) 




