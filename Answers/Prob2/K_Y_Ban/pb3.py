# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:12:20 2017

@author: Bany
"""
import numpy as np
import random as rd

n = int(input("Rock : 1, Scissors : 2, Paper : 3 \n Please input  = ")) # input users choice

L = rd.randrange(1,4) # random 1,2,3

if(L==1):  # if rock
    print("Computer shows Rock \n")
    if(n==2):
        print("You Lose! :( ")
    if(n==3):
        print("You Win! :) ")
            
if(L==2):  # if scissors
    print("Computer shows Scissors \n")
    if(n==3):
        print("You Lose! :( ")    
    if(n==1):
        print("You Win! :) ")
            
if(L==3):  # if paper
    print("Computer shows Paper \n")    
    if(n==1):
        print("You Lose! :( ")
    if(n==2):
        print("You Win! :) ")
            
if(L==n):  # draw
    print("You draw! :|") 
    