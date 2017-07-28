# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:19:47 2017

@author: Bany
"""

class Trinary(object):
    
    def __init__(self, elt):
        if(elt not in ['a','b','c']):
            self.e = 'a'
            print('Trinary must be in [a,b,c]')
            print("Set default 'a'")
        else:
            self.e = elt
            
    def __add__(self, other):
        if self.e=='a':
            if other.e=='a':
                return Trinary('c')
            elif other.e=='b':
                return Trinary('c')
            else:
                return Trinary('b')
        elif self.e=='b':
            if other.e=='a':
                return Trinary('c')
            elif other.e=='b':
                return Trinary('a')
            else:
                return Trinary('a')
        else:
            if other.e=='a':
                return Trinary('b')
            elif other.e=='b':
                return Trinary('a')
            else:
                return Trinary('b')
            
    def __mul__(self,other):
        if self.e=='a':
            if other.e=='a':
                return Trinary('a')
            elif other.e=='b':
                return Trinary('a')
            else:
                return Trinary('a')
        elif self.e=='b':
            if other.e=='a':
                return Trinary('a')
            elif other.e=='b':
                return Trinary('b')
            else:
                return Trinary('c')
        else:
            if other.e=='a':
                return Trinary('a')
            elif other.e=='b':
                return Trinary('c')
            else:
                return Trinary('b')
            
    def __pow__(self, num):
        if num==1:
            return self
        else:
            return self*self**(num-1)
            
    def __str__(self):
        return self.e + '[Trinary]'
    
    

    
    
    
    
    
    
    
    
    