<h1 style="text-align:center">Problem 4</h1>

## 1. Pi (Monte Carlo)
<p style="text-align:right">Provided by <b>Tae Geun Kim</b>

In 2D, there is a well known way to calculate pi with Monte Carlo simulation. Make circle & square which covers circle.
If you throw a ball in a square then the probability of ball in circle is pi*r^2 /4r^2 = pi/4. Thus, you can calculate pi numerically in principle. Then also, we can obtain pi in 3D as same as 2D. 

1. Find pi using Monte Carlo simulation in 2D and 3D to reach 10%, 1%, 0.1% errors. How many times did you throw ball to reach that value? And how long did it take? (time)

2. What is more effective? And why did you think so?
<br>

## 2. More than order 5
<p style="text-align:right">Provided by <b>Tae Geun Kim</b>

We can't obtain analytic solution of polynomial equation which has order more than (or equal) 5. But we can obtain numerically. There are so many methods to find root, so choose one of them. (Or your own method is also possible.)

0. Make find root function
1. Generate 6 random integers in range -5<= x <= 5(ex: -1, 3, 2, -4, 5, 0)
2.  Make polynomial with step 1 (ex: - x^5 + 3x^4 + 2x^3 - 4x^2 + 5x)
3. Find all roots of polynomial and complare it with plot of polynomial
4. At least, test your function more than 5 times.