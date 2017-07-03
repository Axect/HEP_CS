<h1 style="text-align:center">HEP-COSMO Coding Study</h1>
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

## 1. Should Prepare Things

1. Install Git
    > * Ubuntu : sudo apt-get install git
    > * Windows : Just Search "Git windows" or "윈도우 Git"

2. Create Github account
    > * <a href="https://github.com" target='blank'>https://github.com</a>

3. If you create account, then please email to me (edeftg@gmail.com) - Contain your ID.

## 2. Use Markdown

* Github can read markdown. Markdown is simple and great tool to explain code
* For example :
> 1. Python
> ```Python
>import numpy as np
>import pylab as plt
>import seaborn as sns
>import pandas as pd
>
> class Derivative:
>   def __init__(self, f):
>       self.f = f
>       self.h = 1e-04
>
>   def Differentiate(self, x):
>       return (self.f(x+self.h) - self.f(x))/self.h
>
>   def __call__(self, x):
>       return Differentiate(x)
>```
> 2. Go 
> ```Go
>package main
>
>import (
>   "fmt"
>   "math"
>)
>
>func Sqrt(x float64) string {
>   if x >= 0 {
>       return fmt.SPrint(math.Sqrt(x))
>   }
>   return Sqrt(-x) + "i"
>}
>```