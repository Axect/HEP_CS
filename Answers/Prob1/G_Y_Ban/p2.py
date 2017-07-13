# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:43:55 2017

@author: Bany
"""

########################## Q2 ##########################
####from math import sin cos... or * ####

print("<Derivative for x^2 for large error>")  # error reference

def x2_dev1(x):  # definition of x^2 derivative
    h = 10**(-5)  # proper h
    return ((x+h)**2 - (x)**2) / h  # def of derivative
a = int(input("Please input a for x^2, a = "))  # input 'a' some point

print("f'(a) = ", x2_dev1(a))  # print f'(a)



print("<Derivative for x^2>")

def x2_dev(x):  # definition of x^2 derivative
    h = 10**(-9)
    return ((x+h)**2 - (x-h)**2) / (2*h)
a1 = int(input("Please input a for x^2, a = "))  # input 'a' some point

print("f'(a) = ", x2_dev(a1))


print("<Derivative for sin(x)>")

def sin_dev(x):  # definition of sin(x) derivative
    import math
    h = 10**(-9)
    return (math.sin(x+h) - math.sin(x-h)) / (2*h)
a2 = int(input("Please input a for sin(x), a = "))  # input 'a' some point

print("f'(a) = ", sin_dev(a2))


print("<Derivative for e^x>")

def e_dev(x):  # definition of e^x derivative
    import math
    h = 10**(-9)
    return (math.e**(x+h) - math.e**(x-h)) / (2*h)
a3 = int(input("Please input a for e^x, a = "))  # input 'a' some point

print("f'(a) = ", e_dev(a3))


print("<Derivative for ln(x)>")

def ln_dev(x):  # definition of ln(X) derivative
    import math
    h = 10**(-9)
    return (math.log(x+2*h) - math.log(x+h)) / h
a4 = int(input("Please input a for ln(x), a = "))  # input 'a' some point

print("f'(a) = ", ln_dev(a4))


