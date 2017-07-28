# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:08:47 2017

@author: Bany
"""

import matplotlib.pyplot as plt  # need to plot


g_con = 6.67259e-11
sun_m = 1.9891e30
ear_m = 5.9736e24
AU = 1.49597870691e11

x0 = -9.851920196143998e-1*AU
y0 = 1.316466809434336e-1*AU
z0 = -4.877392224782687e-6*AU

x1 = -9.864337701483683e-1*AU
y1 = 1.230799243164879e-1*AU
z1 = -4.374019384763304e-6*AU

dt = 43200.0
xv0 = (x1-x0)/43200.0
yv0 = (y1-y0)/43200.0
zv0 = (z1-z0)/43200.0


def a_x(x,y,z):
    
    return g_con*sun_m*(-x)/((x**2+y**2+z**2)**1.5)

def a_y(x,y,z):
    
    return g_con*sun_m*(-y)/((x**2+y**2+z**2)**1.5)

def a_z(x,y,z):
    
    return g_con*sun_m*(-z)/((x**2+y**2+z**2)**1.5)

def k_1(x0,y0,z0,x1,y1,z1):
    kx = (x1-x0)/dt
    ky = (y1-y0)/dt
    kz = (z1-z0)/dt
    
    return (kx,ky,kz)

def kv_1(x1,y1,z1):
    kvx = a_x(x1,y1,z1)
    kvy = a_y(x1,y1,z1)
    kvz = a_z(x1,y1,z1)
    
    return (kvx,kvy,kvz)

def k_2(x1,y1,z1,xv,yv,zv):
    kx = xv + dt*a_x(x1,y1,z1)/2
    ky = yv + dt*a_y(x1,y1,z1)/2
    kz = zv + dt*a_z(x1,y1,z1)/2

    return (kx,ky,kz)
    
def kv_2(x1,y1,z1,kx,ky,kz):
    kvx = a_x(x1+dt*kx/2,y1+dt*ky/2,z1+dt*kz/2)
    kvy = a_y(x1+dt*kx/2,y1+dt*ky/2,z1+dt*kz/2)
    kvz = a_z(x1+dt*kx/2,y1+dt*ky/2,z1+dt*kz/2)    
    
    return (kvx,kvy,kvz)

def k_3(xv,yv,zv,kvx,kvy,kvz):
    kx =  xv + dt*kvx/2
    ky =  yv + dt*kvy/2
    kz =  zv + dt*kvz/2
    
    return (kx,ky,kz)    

def kv_3(x1,y1,z1,kx,ky,kz):
    kvx = a_x(x1+dt*kx/2,y1+dt*ky/2,z1+dt*kz/2)
    kvy = a_y(x1+dt*kx/2,y1+dt*ky/2,z1+dt*kz/2)
    kvz = a_z(x1+dt*kx/2,y1+dt*ky/2,z1+dt*kz/2)
    
    return (kvx,kvy,kvz)

def k_4(xv,yv,zv,kvx,kvy,kvz):
    kx =  xv + dt*kvx
    ky =  yv + dt*kvy
    kz =  zv + dt*kvz
    
    return (kx,ky,kz)    

def kv_4(x1,y1,z1,kx,ky,kz):
    kvx = a_x(x1+dt*kx,y1+dt*ky,z1+dt*kz)
    kvy = a_y(x1+dt*kx,y1+dt*ky,z1+dt*kz)
    kvz = a_z(x1+dt*kx,y1+dt*ky,z1+dt*kz)  
    
    return (kvx,kvy,kvz)

x_list = [x0,x1]
y_list = [y0,y1]
z_list = [z0,z1]

xv_list = [xv0]
yv_list = [yv0]
zv_list = [zv0]

k_list = []
u_list = []
e_list = []

ax0 = a_x(x1,y1,z1)
ax_list = [ax0]


for i in range(int(3650*24*3600/dt)):
    k1x,k1y,k1z = k_1(x_list[i],y_list[i],z_list[i],x_list[i+1],y_list[i+1],z_list[i+1])
    k1vx,k1vy,k1vz = kv_1(x_list[i+1],y_list[i+1],z_list[i+1])
    
    k2x,k2y,k2z = k_2(x_list[i+1],y_list[i+1],z_list[i+1],xv_list[i],yv_list[i],zv_list[i])
    k2vx,k2vy,k2vz = kv_2(x_list[i+1],y_list[i+1],z_list[i+1],k1x,k1y,k1z)
    
    k3x,k3y,k3z = k_3(xv_list[i],yv_list[i],zv_list[i],k2vx,k2vy,k2vz)
    k3vx,k3vy,k3vz = kv_3(x_list[i+1],y_list[i+1],z_list[i+1],k2x,k2y,k2z)    
    
    k4x,k4y,k4z = k_4(xv_list[i],yv_list[i],zv_list[i],k3vx,k3vy,k3vz)
    k4vx,k4vy,k4vz = kv_4(x_list[i+1],y_list[i+1],z_list[i+1],k3x,k3y,k3z)      
    
    
    x_list.append(x_list[i+1] + dt*(k1x+2*k2x+2*k3x+k4x)/6.0)
    xv_list.append(xv_list[i] + dt*(k1vx+2*k2vx+2*k3vx+k4vx)/6.0)    

    y_list.append(y_list[i+1] + dt*(k1y+2*k2y+2*k3y+k4y)/6.0)
    yv_list.append(yv_list[i] + dt*(k1vy+2*k2vy+2*k3vy+k4vy)/6.0)    

    z_list.append(z_list[i+1] + dt*(k1z+2*k2z+2*k3z+k4z)/6.0)
    zv_list.append(zv_list[i] + dt*(k1vz+2*k2vz+2*k3vz+k4vz)/6.0)  
    
    ax_list.append(a_x(x_list[i+2],y_list[i+2],z_list[i+2]))

    k_list.append(0.5*ear_m*(xv_list[i]**2+yv_list[i]**2+zv_list[i]**2))
    u_list.append((-g_con*sun_m*ear_m)/(2*((x_list[i]**2+y_list[i]**2+z_list[i]**2)**0.5)))
    e_list.append(k_list[i]+u_list[i])

print(x_list[-1]/AU,y_list[-1]/AU,z_list[-1]/AU)

"""
plt.plot(x_list,label='x-axis')
plt.plot(y_list,label='y-axis')
plt.plot(z_list,label='z-axis')
"""
plt.plot(k_list)
plt.plot(u_list)
plt.plot(e_list)


plt.xlabel('time')  # x-axis
plt.ylabel('x/y/z')  # y-axis
plt.title('Dangerous')  # title
plt.show()  # plot show












