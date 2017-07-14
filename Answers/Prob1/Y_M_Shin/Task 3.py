# -*- coding: utf-8 -*-
"""
Task 3
"""

"""
loop calculation
"""
import time

measure1 = 0
    
for count1 in range(1,11):
    
    start1 = time.time()
    tot1 = 0
    
    for x1 in range(1,10**6+1):
        tot1 = tot1 + x1

    end1 = time.time()
    print(tot1)
    print("=>", end1 - start1,"s")
    measure1 = measure1 + (end1 - start1)
   
    count1 = count1 + 1

    
print("Average time for loop calculation:", measure1/10)

print("--------------------------")

"""
module calculation
"""
import numpy as np

measure2 = 0

for count2 in range(1,11):
    start2 = time.time()

    ary = np.arange(1,10**6+1,dtype = np.float)
    tot2 = np.sum(ary)

    end2 = time.time()
    print(tot2)
    print("=>", end2 - start2, "s")
    measure2 = measure2 + (end2 - start2)
    count2 = count2 + 1

print("Average time for module calculation:", measure2/10)

if measure1 < measure2:
    print("loop calculation is faster by", (measure2 - measure1)/10, "seconds")
    
elif measure2 < measure1:
    print("NumPy calculation is faster by", (measure1 - measure2)/10, "seconds")
    
else:
    print("both have the same calculation time")