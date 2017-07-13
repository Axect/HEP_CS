# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:44:35 2017

@author: Bany
"""

########################## Q3 ##########################
import datetime 
import numpy

L = range(1,10**6+1)


def SUM_L(L):  # Calculate by loop method
    S = 0 # start
    start = datetime.datetime.now()  # check start time
    for i in range(len(L)): 
        S = S+L[i]      
    end = datetime.datetime.now()  # check end time
    
    print("Running time by loop method : " , end-start)  # calculate running time

def SUM_N(L):  # Calculate by numpy method

    start = datetime.datetime.now()  # check start time
    S = numpy.sum(L)
    end = datetime.datetime.now()   # check end time
    
    print("Running time by numpy method : " , end-start)  # calculate running time


for i in range(10):  # running 10 times
    SUM_L(L)
    SUM_N(L)
