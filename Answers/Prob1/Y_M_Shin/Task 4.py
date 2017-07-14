# -*- coding: utf-8 -*-
"""
task 4
"""
import numpy as np
import matplotlib.pyplot as plt
import math

valx = float(input("value for x value: "))
if valx >= -1 and valx <= 1:   
    valy = math.sqrt(1-valx**2)
    
    def Circle(x,y):
       return (x*x+y*y)

    xx=np.linspace(-2,2,400)
    yy=np.linspace(-2,2,400)
    [X,Y]=np.meshgrid(xx,yy)

    Z=Circle(X,Y)

    plt.figure()
    plt.contour(X,Y,Z,[1])
    plt.contour(x.ravel(), y.ravel(), y*valy + x*valx, [1])
    plt.contour(x.ravel(), y.ravel(), -y*valy + x*valx, [1])
    plt.grid()
    plt.show()
else:
    print("invalid x")
    