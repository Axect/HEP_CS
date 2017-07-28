#Open data from csv to plot
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn

with open("Orbit.csv", "r", newline = "") as f:
    fopen = list(csv.reader(f))

    t = [i for i in range(7300+1)]
    X = [i[0] for i in fopen] 
    Y = [i[1] for i in fopen]
    Z = [i[2] for i in fopen]

    plt.title("Orbit")
    plt.plot(t, X, label = 'x')
    plt.plot(t, Y, label = 'y')
    plt.plot(t, Z, label = 'z')
    plt.legend(loc='upper left')
    plt.xlabel('time in tscale = 43200 sec')
    plt.ylabel('X Y Z')
    plt.savefig("Orbit.png")

f.close()

with open("Energy.csv", "r", newline = "") as g:
    fopen2 = list(csv.reader(g))
    
    t = [i for i in range(7300+1)]
    KE = [i[0] for i in fopen2]
    PE = [i[1] for i in fopen2]
    Et = [i[2] for i in fopen2]

    plt.title("Energy")
    plt.plot(t, KE, label = 'KE')
    plt.plot(t, PE, label = 'PE')
    plt.plot(t, Et, label = 'Total')
    plt.legend(loc='upper left')
    plt.xlabel('time in tscale = 43200 sec')
    plt.ylabel('Energy(J)')
    plt.savefig("Energy.png")

with open("Orbit_reverse.csv", "r", newline = "") as f:
    fopen = list(csv.reader(f))

    t = [i for i in range(7300+1)]
    X = [i[0] for i in fopen] 
    Y = [i[1] for i in fopen]
    Z = [i[2] for i in fopen]

    plt.title("Orbit Reverse")
    plt.plot(t, X, label = 'x')
    plt.plot(t, Y, label = 'y')
    plt.plot(t, Z, label = 'z')
    plt.legend(loc='upper left')
    plt.xlabel('time in tscale = 43200 sec')
    plt.ylabel('X Y Z')
    plt.savefig("Orbit Reverse.png")
    

with open("Energy_reverse.csv", "r", newline = "") as g:
    fopen2 = list(csv.reader(g))
    
    t = [i for i in range(7300+1)]
    KE = [i[0] for i in fopen2]
    PE = [i[1] for i in fopen2]
    Et = [i[2] for i in fopen2]

    plt.title("Energy Reverse")
    plt.plot(t, KE, label = 'KE')
    plt.plot(t, PE, label = 'PE')
    plt.plot(t, Et, label = 'Total')
    plt.legend(loc='upper left')
    plt.xlabel('time in tscale = 43200 sec')
    plt.ylabel('Energy(J)')
    plt.savefig("Energy Reverse.png")
