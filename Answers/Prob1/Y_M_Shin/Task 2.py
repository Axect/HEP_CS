# -*- coding: utf-8 -*-
"""
Task 2
"""

h=0.000001
print("h=", h)

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    
print("Differentiation of x^2: ")
n1 = ((h**2)-0)/h
print(n1)

print("Differentiation of sin(x): ")
sin2 = 0
for k in range(0,10):
    sin2 = sin2 + ((-1)**k)*(h**(2*k + 1))/fac(2*k + 1)
n2 = (sin2-0)/h
print(n2)

print("Differentiation of exp(x): ")
e3 = 0
for m in range(0,100):
    e3 = e3 + (h**m)/fac(m)
n3 = (e3-1)/h
print(n3)

print("Differentiation of ln(x): ")
u = -1
uu = -1 + h
ln4 = 0
ln5 = 0
for n in range(0,100):
    ln4 = ln4 + ((-1)**n)*(u**(n+1))/(n+1)
    
for p in range(0,100):
    ln5 = ln5 + ((-1)**p)*(uu**(p+1))/(p+1)
n4 = (ln5 - ln4)/h
print(n4)