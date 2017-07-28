# -*- coding: utf-8 -*-
"""
Task 2, Take 2


"""

import math
import matplotlib.pyplot as plt
import time

AU = 1.49597870691e+11
m = 5.9736E24 # Mass of Earth
M = 1.9891E30 # Mass of Sun
G = 6.67259E-11 # Gravitational constant

interval = 43200 # Time interval = 12 hours

# Initial position
x1 = -9.851920196143998E-01 * AU
y1 = 1.316466809434336E-01 * AU
z1 = -4.877392224782687E-06 * AU

class Vector(object):
    def __init__(self, x, y, z): # Initialize
        self.x = x
        self.y = y
        self.z = z
        self.size = math.sqrt(x**2 + y**2 + z**2) # Size of the vector
        if self.size == 0: # If the size of the vector is 0, normal components are 0
            self.nx = 0
            self.ny = 0
            self.nz = 0
        else: # Calculate normal vector components
            self.nx = x / self.size
            self.ny = y / self.size
            self.nz = z / self.size
    
    def __add__(self, other): # Define addition of vectors
        if type(other) == type(self):
            return [self.x + other.x, self.y + other.y, self.z + other.z]
    def __sub__(self, other): # Define subtraction of vectors
        return [self.x - other.x, self.y - other.y, self.z - other.z]
    
    def __mul__(self, other): # Define multiplication of Vector*Vector or Vetor*number
        if type(other) == type(self):
            return Vector((self.x)*(other.x), (self.y)*(other.y), (self.z)*(other.z))
        elif type(other) == float or type(other) == int:
            return Vector((self.x)*other,(self.y)*other,(self.z)*other)
    
    def __rmul__(self, other): # Define reverse multiplication
        return self.__mul__(other)
        
    def __mod__(self, other): # A%B is the difference vector
        D = Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return D
    
    def __matmul__(self, other): # A@B is the distance between the two vectors
        D = self%other
        return math.sqrt((D.x)**2 + (D.y)**2 + (D.z)**2)
    
    def __floordiv__(self, other): # A//B is dividing vectors between vectors & scalars
        if type(other) == type(self):
            return Vector((self.x)/(other.x), (self.y)/(other.y), (self.z)/(other.z))
        elif type(other) == int or type(other) == float:
            return Vector((self.x)/other, (self.y)/other, (self.z)/other)
    
    def __rfloordiv__(self, other): # Define reverse A//B
        return self.__floordiv__(other)
        
    def __str__(self): # Define Print
        return str([self.x, self.y, self.z])
    
    def Eacc(P): # Calculate the acceleration vector of Earth at position vector P
        a = G*M/((P.size)**2)
        A = Vector(-a * (P.nx), -a * (P.ny), -a * (P.nz))
        return A
    
    def KE(V): # Calculate the kinetic energy of Earth with velocity vector V
        return (1/2) * m * (V.size)**2
    
    def PE(P): # Calculate the potential energy of Earth at position vector P
        return -G * M * m / (P.size)
    
    def NextP(P,V): # Determine next position.
        P.x += interval * (V.x)
        P.y += interval * (V.y)
        P.z += interval * (V.z)
        NEWP = Vector(P.x, P.y, P.z)
        return NEWP

    def NextV(P,V): # Determine next velocity
        V.x += interval * Vector.Eacc(P).x
        V.y += interval * Vector.Eacc(P).y
        V.z += interval * Vector.Eacc(P).z
        NEWV = Vector(V.x, V.y, V.z)
        return NEWV
    
    def BackP(P,V): # Determine position backwards.
        P.x -= interval * (V.x)
        P.y -= interval * (V.y)
        P.z -= interval * (V.z)
        NEWP = Vector(P.x, P.y, P.z)
        return NEWP

    def BackV(P,V): # Determine velocity backwards.
        V.x -= interval * Vector.Eacc(P).x
        V.y -= interval * Vector.Eacc(P).y
        V.z -= interval * Vector.Eacc(P).z
        NEWV = Vector(V.x, V.y, V.z)
        return NEWV
    
start = time.time()
X0 = Vector(x1,y1,z1)
V0 = Vector(-4171.266792883339, -29683.150695830704, 1.7437743811073216)

KEE = []
PEE = []
Energy = []
Xpos = []
Ypos = []

print("Initial position:", X0 // AU)
print("Initial velocity:", V0)
print("=======================================")
for i in range(1,7301):
    #Calculate KE, PE and KE + PE to make a list.
    newp = Vector.PE(X0)
    newk = Vector.KE(V0)
    PEE.append(newp)
    KEE.append(newk)
    Energy.append(newp + newk)
    
    # Calculate next position and velocity
    Xpos.append(X0.x / AU)
    Ypos.append(X0.y / AU)
    XX = X0
    VV = V0
    X0 = Vector.NextP(XX,VV)
    V0 = Vector.NextV(X0,VV)    

    i = i + 1
    
#Print out final position
print("Final position:", X0 // AU)
print("Final velocity:", V0)
print("=======================================")

#Plot Orbit and Energies
plt.figure(1)
plt.subplot(1,1,1)
plt.plot(Xpos, Ypos, 'k')
plt.xlabel('X position [AU]')
plt.ylabel('Y position [AU]')
plt.title('X-Y Position of Earth')
plt.grid(True)
plt.show()

plt.figure(2)
plt.plot(PEE, label = 'Potential')
plt.plot(KEE, label = 'Kinetic Energy')
plt.plot(Energy, label = 'Total Energy')
plt.xlabel('Time interval [0.5 days]')
plt.ylabel('Energy [J]')
plt.ylim(-6E33,6E33)
plt.grid(True)
plt.legend()
plt.show()

print("=======================================")
print("Retracing back from final point")
print("=======================================")

Xpos = [] # Initialize
Ypos = [] # Initialize
for i in range(1,7301):
    # Calculate next position and velocity BACKWARDS
    Xpos.append(X0.x / AU)
    Ypos.append(X0.y / AU)
    XX = X0
    VV = V0
    X0 = Vector.BackP(XX,VV)
    V0 = Vector.BackV(X0,VV)    

    i = i + 1

print("Final position:", X0 // AU)
print("Final velocity:", V0)
print("=======================================")

plt.figure(3)
plt.plot(Xpos, Ypos, 'k')
plt.xlabel('X position [AU]')
plt.ylabel('Y position [AU]')
plt.title('X-Y Position of Earth: BACKWARDS')
plt.grid(True)
plt.show()

KEE = []
PEE = []
Energy = []
Xpos = []
Ypos = []

end = time.time()

print("Total time: {} s".format(end - start))
# It is much faster when you make a list with a certain length rather than using append.
# Runge - Kutta Method
#Verlet method

    