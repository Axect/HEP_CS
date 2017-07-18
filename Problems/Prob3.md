<h1 style="text-align:center">Problem 3</h1>
<h3 style="text-align:center">Focused on OOPs</h3>
<br>

## 1.  Make Trinary Group
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

### 1) Prepare Class
* Make Trinary Class (or Type) 
    * There are only 3 distinguishable elements {a, b, c} (like {0,1,2})

### 2) Define Methods
* Add(```__add__```) : a+b=c, b+c=a, c+c=b and etc.
* Multiply : ab=a, bc=c, c^2=b and etc.
* Square : Same as Multiply.
* String(```__str__```) : ```A=Trinary{2(or b)}; Print(A) -> 2 (or b) [Trinary]```

### 3) Example Code (Main)
``` Go
func main() {
    A, B, C := Trinary{0}, Trinary{1}, Trinary{2}
    Print(A + B) // Output: 1 [Trinary]
    Print(C^2) // Output: 2 [Trinary]
}
```
<br>

