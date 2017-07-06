<h1 style="text-align:center"> Problem 1 </h1>

## 1. Harmonic Oscillator
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

```latex
E_n = \hbar\omega(n+1/2)
```

* Put \omega = 1
* Input n, output E_n by using \hbar (n > 0, \hbar -> h)
* <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/aa5a2ba0277fc95bf1b3f3cb37138a13ad376ac7">
* Using above value, make converter which represents E_n with eV

## 2. Differentiate
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

* Given function & point output f'(x)
    * Test x^2, sin(x), e^(x), ln(x) at x = 0
* How to reduce the error?

## 3. Effective Sum List
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

* Given list, output Sum (integer)
    * List = 1 ~ 1e+06 (1 milion)
    * Calculate sum by for loop
    * Calculate sum with some modules (e.g numpy)
* Obtain elapsed time
    * time for for loop 10 times
    * time for module 10 times
    * Compare them and print results as pretty

## 4. Basic circle plot with tangent line
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

```latex
circle : x^2 + y^2 = 1
tangent line : x_1x + y_1y = 1
```
* Using above eqs, given point (x_1, y_1), draw the plot circle & tangent line.