<h1 style="text-align:center">Problem 4</h1>

## 1. Pi (Monte Carlo)
<p style="text-align:right">Provided by <b>Tae Geun Kim</b>

In 2D, there is a well known way to calculate pi with Monte Carlo simulation. Make circle & square which covers circle.
If you throw a ball in a square then the probability of ball in circle is pi*r^2 /4r^2 = pi/4. Thus, you can calculate pi numerically in principle. Then also, we can obtain pi in 3D as same as 2D. 

1. Find pi using Monte Carlo simulation in 2D and 3D to reach 10%, 1%, 0.1% errors. How many times did you throw ball to reach that value? And how long did it take? (time)

2. What is more effective? And why did you think so?
<br>

## 2. Numerical Root Finding
<p style="text-align:right">Provided by <b>Tae Geun Kim</b>

For many cases, we can't find root of some equations analytically. Thus, we should find root numerically.

1. Make find root function
2. Test that fuction for some eqs & Obtain number of runnings to err < 1e-10
    * x^2 - 4 = 0
    * x^3 - 6x^2 + 11x -6 = 0
3. Find root for some eqs :
    * x - cosx = 0
    * x^3 - cosx = 0
4. Do anything else