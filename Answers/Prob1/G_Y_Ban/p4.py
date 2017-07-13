# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:44:40 2017

@author: Bany
"""

########################## Q4 ##########################

import matplotlib.pyplot as plt  # need to plot
import numpy as np  # need to arange

x = np.arange(-1,1.0001,0.0001) # 20000 spots
f = np.arange(-2,2.0001,0.0001) # 40000 spots

x1 = float(input("Please input x1=")) # given point x1
y1 = float(input("Please input y1=")) # given point y1

y_1 = (1-x**2)**(0.5)  # upper circle
y_2 = -(1-x**2)**(0.5)   # lower circle

y = -x1*f/y1 + 1/y1  # tangent line


plt.figure(figsize=(8, 8), dpi=100)  # plot
plt.xlim(-2,2)  # x-axis range
plt.ylim(-2,2)  # y-axis range
plt.plot(x,y_1,label='Upper Circle')  # circle-label
plt.plot(x,y_2,label='Lower Circle')  # circle-label
plt.plot(f,y,label="Tagent line")  # line-label
plt.xlabel('x')  # x-axis
plt.ylabel('y')  # y-axis
plt.title('Unit circle')  # title
plt.grid()  # grid
plt.legend()  # for label
plt.show()  # plot show
