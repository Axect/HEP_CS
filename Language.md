<h1 style="text-align:center">Choose Programming Languages</h1>
<h2 style="text-align:center">For Physicists</h2>
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

## 1. Candidates

| Languages | Advantages | Disadvantages|
| -----------------|-------------------|----------------------|
|Mathematica| Easy to Use, Powerful Symbolic| Slow, Can't Customize, Expensive|
|Matlab           | Easy to Use, Good Vector Operation|Slow, Bad to customize|
| R | Easy to Use, Many Tools | Very Slow, Strange|
| Python | Easy to Use, Many Tools, Easy to Custmize | Slow|
|  Julia | High performance, Good to Data Science | Young, Few Documents|
| Go | High Speed, High Concurrency | Few libraries for Data Science|
| Java | It is Java | It is Java|
| Rust | High performance, High Concurrency | Difficult to use|
| C++ | High performance, Many libraries | Dirty, Too Long Codes|
| Fortran | Very high performance, Scientific | Die|
| C | High performance, Many libraries | Too Long Codes|

## 2. Classify Languages

1. Easy
    > Mathematica > Matlab > R > Python > Julia >> Go > Java > Rust > C > C++ >> Fortran

2. Speed
    > C ~ Fortran > C++ ~ Rust > Go ~ Julia > Java >>> Python > Matlab > Mathematica > R
    >
    > -Reference : <a href="http://benchmarksgame.alioth.debian.org/u64q/performance.php?test=nbody&sort=elapsed" target="_blank">Speed Benchmark Game</a>
    > | Test | 포트란 | 줄리아 | 파이썬 | R | 매트랩 |  매스매티카 | Go | 자바 |
    > |-----| ----|-----|-----|---|-----|-------|----|---|
    > ||gcc 5.1.1 | 0.4.0 | 3.4.3 | 3.2.2 | R2015b |  10.2.0 | go1.5 | 1.8.0_45
    > | fib | 0.70 | 2.11 | 77.76 | 533.52 | 26.89 |  118.53 | 1.86 | 1.21 |
    > | parse_int | 5.05 | 1.45 | 17.02 | 45.73 | 802.52 | 15.02 | 1.20 | 3.35 |
    > | quicksort | 1.31 | 1.15 | 32.89 | 264.54 | 4.92 | 43.23 | 1.29 | 2.60 |
    > | mandel | 0.81 | 0.79 | 15.32 | 53.16 | 7.58 | 5.13 | 1.11 |  1.35 |
    > | pi_sum | 1.00 | 1.00 | 21.99 | 9.56 | 1.00 |  1.69 | 1.00 |  1.00 |
    > | rand_mat_stat | 1.45 | 1.66 | 17.93 | 14.56 | 14.52 |5.95 | 2.96 |  3.92 |
    > | rand_mat_mul | 3.48 | 1.02 | 1.14 | 1.57 | 1.12 | 1.30 | 1.42 |  2.36 |


3. Physics Libraries (Particle Physics)
    > C/C++ > Mathematica >> Python >>> Go(Little bit) > And Others


4. Some Rankings
    > <a href="https://www.slant.co/topics/25/~best-programming-language-to-learn-first" target="_blank">- What are the best languages to learn first</a>  
    > <a href="https://www.slant.co/topics/4001/~programming-languages-for-data-science" target="_blank">- What are the best languages for Data Science</a>  
    > <a href="https://www.slant.co/topics/5984/~productivity-enhancing-well-designed-and-concise-rather-than-just-popular-or-time-tested-programming-la" target="_blank">- What are the best languages for productivity</a>

## 3. Question to Determine Programming Languages

1. What's your primary  language?
    > * C or C++ : Use C, C++ or Rust
    > * Matlab or R : Use Python or Julia
    > * Python : Use Go or Julia
    > * Nothing : Use Python or Mathematica /  Study C/C++

2. What's your coding level?
    > -Can you calculate sum of some sequences?  (No :  Zero)  
    > -Do you know OOPs or Functional Programming? (No : Low)  
    > -Can you use pointer? (No : Intermediate)  
    > -Can you use type and method? (No : Intermediate)
    > * Zero : Use Mathematica or Matlab or Python
    > * Low : Study C/C++ or Python / Challenge Julia
    > * Intermediate : Study Go or Rust / Use Julia or Python or C/C++
    > * Else : Do anything

## 4. Conclusion

> Personally, I recommend **Julia** to future Physicists. But there are many libraries written by **C++**, so you should study **C++** if you want to become experimental Physicist. If you don't have any programming experiences, then you'd better to study **Python** first. If you hate programming, then **Mathematica** is the best solution.  