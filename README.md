<h1 style="text-align:center">HEP-COSMO Coding Study</h1>
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

## 1. Create Github Account

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

* All of this code is written by Markdown. (And even this document also)
* You should learn markdown to use github

## 3. Git

1. Create repository at Github (No initialize)
2. Make some directory on your computer (e.g SM)
3. Make any files (e.g Higgs.txt)
4. Should initialize your folder as follows:
    > 1. git init
    > 2. git remote add Any_Name(e.g origin) https://github.com/Your_Github_ID/Repository_Name
    > 3. git config --global user.name Your_Name
    > 4. git config --global user.email Your_Email
    > 5. git add Higgs.txt
    > 6. git commit -am "Any_Message(Add some file or fix some file)"
    > 7. git push Any_Name(From ii.) master
5. Now you can use git & github. Here is the brief manual:
    > * If you fix file only :
    >   * git commit -am "Log_Message"
    >   * git push Any_Name master
    > * If you add some file to directory :
    >   * git add File_Name
    >   * git commit -am "Log_Message"
    >   * git push Any_Name master 