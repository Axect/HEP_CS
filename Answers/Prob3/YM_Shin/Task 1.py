fgo# -*- coding: utf-8 -*-
"""
Task 1
"""

class Ternary(object):

    def __init__(self, element): # Make element Ternary
        self.element = element % 3
        
    def __add__(self, other): # Define '+'
        return (self.element + other.element) % 3
    
    def __sub__(self,other): # Define '-'
        return (self.element - other.element) % 3
        
    def __mul__(self, other): # Define '*'
        return (self.element * other.element) % 3
    
    def __xor__(self, sq): # Define '^'
       if self.element == 0: # Base 0 is not defined
           return "Error"     
       else:
               if sq == 0: # If exponent = 0 the result is 1
                   return 1
               elif sq < 0: # Negative exponents are not defined in Ternary group
                   return "Error"
               else:
                   sq = int(sq)
                   for i in range(1, sq):
                       self.element = self.element * self.element
                       i = i + 1
                   return self.element % 3
    
    def __str__(self): # Define print
        return "{}".format(self.element)
    
A = Ternary(0)
B = Ternary(1)
C = Ternary(2)
D = Ternary(5) # Ternary(5) = 2
print(A.element)
print(C^(-1))
print(D)

