# -*- coding: utf-8 -*-
"""
Task one
"""
import random
import time
count = 0 # Variable for counting the # of times quincunx appears.

start = time.time()
for n in range(1,10**6+1): # n counts the # of times of rolling the dice.
    
    k = random.randrange(1,7)
    if k == 5: # If quincunx appears, count.
        count = count + 1
        n = n + 1
    else: # If not, don't.
        n = n + 1
end = time.time() # Measure the time that it took for rolling the dice.

print("Elapsed time:", end - start, "s")
print("Quincunx appeared", count,"times out of one million rolls")
print("Probabiltiy for quincunx: ", count/n)
print("Theoretical expectation: ", 1/6)

# Determine whether the result is higher or lower than expected.
if 1/6 > count/n:
    print("Result is", 10/6 - (10*count/n), "% lower than expected")
elif 1/6 < count/n:
    print("Result is", (10*count/n) - 10/6, "% higher than expected")
else:
    print("Perfectly agrees with expectation")