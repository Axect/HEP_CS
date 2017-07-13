# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:44:40 2017

@author: Bany
"""

########################## Q1 ##########################

print("<Harmonic Oscillator Energy>")  # title
n = int(input("Please input n="))   # input 'n' s.t integer
h = 6.582*10**(-16)
ha = "h"  # letter of 'h'

def energy(n): # definition of energy function

    if (n>=0) : # n is positive
        E=n+0.5
        print("E_n = " , E , ha ) # print E with h
        print("E_n(eV) = \n" , E*h) # print E with eV
    elif (n<0) : # if n is not positive integer
        print("n must be positive integer, plz retry \n")    
        
energy(n) # function running

