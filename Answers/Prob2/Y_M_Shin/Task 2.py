# -*- coding: utf-8 -*-
"""
Task 2
"""
import csv
import numpy as np
from scipy.stats import rankdata
import matplotlib.pyplot as plt

score = [64, 90, 98, 100, 92, 90, 91, 72, 88, 93, 93, 52]
rank = len(score) - rankdata(score, method = 'min') # Ranks are determined in reverse

for i in range(0,12):
    rank[i] = rank[i] + 1
    i = i + 1

mean = np.mean(score) # Mean value calculated
std = np.std(score) # Standatd deviation calculated
print("mean:", mean)
print("STD:", std)

f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(["Schrodinger", 64, rank[0]])
wr.writerow(["Einstein", 90, rank[1]])
wr.writerow(["Feynman", 98, rank[2]])
wr.writerow(["Neumann", 100, rank[3]])
wr.writerow(["Dirac", 92, rank[4]])
wr.writerow(["Bohr", 90, rank[5]])
wr.writerow(["Fermi", 91, rank[6]])
wr.writerow(["Heisenberg", 72, rank[7]])
wr.writerow(["Pauli", 88, rank[8]])
wr.writerow(["Newton", 93, rank[9]])
wr.writerow(["Leibniz", 93, rank[10]])
wr.writerow(["Planck", 52, rank[11]])
f.close()

with open('output.csv') as data: # Read only the first column
    reader = csv.reader(data)
    first_column  = next(zip(*reader))

x, y = np.loadtxt('output.csv', usecols = (1,2), unpack = True, delimiter = ',') # Read only 2nd, 3rd column
ind = np.arange(len(y))
plt.bar(ind, x)
plt.xticks(ind,first_column)