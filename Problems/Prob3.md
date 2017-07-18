<h1 style="text-align:center">Problem 3</h1>

<br>

## 1.  Make Trinary Group (OOP)
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

## 2. Orbit of the Earth (Numerical Integration)
<p style="text-align:right">Provided by <b>Yong Woo Kim</b></p>

Write function that simulates the orbit of Earth around sun.  The sun is located at the origin (0,0,0) and is considered fixed point.
Mass of Earth and Sun, and Gravitational constant G are given below.
```
Gravitational constant G = 6.67259e-11(N*m^2/kg^2)
Earth mass m = 5.9736e24(kg)
Sun mass M = 1.9891e30(kg)
1AU = 1.49597870691E+11 m
```
Two Earth positions at different time are given below (3D coordinates).

```
(-9.851920196143998E-01, 1.316466809434336E-01, -4.877392224782687E-06) (AU),
at 00:00, March. 13, 2013
(-9.864337701483683E-01, 1.230799243164879E-01, -4.374019384763304E-06) (AU)
at 12:00, March. 13, 2013
```
Using given data, do time integration numerically with timestep Δt=43200(sec) . You can use any integration algorithm.

1. What is the Earth position in (x,y,z) after 3650 days?
2. Plot x position of Earth in time t during 3650 days.
3. Plot kinetic energy(E_k), potential energy(E_p) and mechanical energy(E_tot) as a function of time t. Is the total energy conserved?
4. Do numerical integration for 3650 days. From that point, now reverse velocity direction of Earth and do time integration during 3650 days. Is the Earth go back to its original position? Whether it is or not, Let us think about the reason.
