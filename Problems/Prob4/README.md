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
(You can refer https://drive.google.com/open?id=0B3uxs1rmaMDTT3RxSWFrdXYzRFE )

1. Make find root function
2. Test that fuction for some eqs - Obtain number of runnings to err < 1e-10
    * x^2 - 4 = 0 for interval [-1, 4] or start with x0=1
    * x^5 -2x^3 -7x^2 +14 = 0 for interval [-3, 1] or start with x0=1
3. Find all roots for some eqn :
    * x - cosx = 0
    * Ai(x) = 0 (Ai is airy function)
4. Do anything else
<br>

## 3. Find Local Maxima of Numerical function
<p style="text-align:right">Provided by <b>Tae Geun Kim</b>

Last time, we obtained orbit of the Earth by numerical integrations. Now, we want to find the point where the highest distance between the Sun and Earth.

1. Write csv file of orbit of the Earth (x, y, z coordinates)

> If you can't trust your data then you can use my data in github.  
> ```git clone https://github.com/Axect/HEP_CS.git```  
> Then you can find my csv data in ```HEP_CS/Answers/Prob3/TG_Kim/prob3/Data/taylor.csv```

2. Find local maxima of distance during 10 years.
3. Find global maximum.
4. Discuss the results.