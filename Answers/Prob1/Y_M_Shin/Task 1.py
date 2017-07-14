# -*- coding: utf-8 -*-
"""
Task one
"""
import math

print("E_n = hbar * omega * (n+1/2)")
number = input("Input positive integer n: ")
n = int(number)

if n == 0: 
    print("E_n =", 1/2,"hbar")
    print("E_n =", 6.582119514*1/2,"E",-16,"eV")
    
elif n > 0:
    num = int(math.log10(6.582119514*n))
    power = -16 + num
    
    print("E_n =", (n+1/2),"hbar")
    print("E_n =", 6.582119514*(n+1/2)/(10**num),"E",power,"eV")
      
else:
    print("Invalid number for n")