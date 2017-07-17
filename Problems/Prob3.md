<h1 style="text-align:center">Problem 3</h1>
<h3 style="text-align:center">Focused on OOPs</h3>
<br>

## 1. Basic Particle Physics
<p style="text-align:right">Provided by <b>Tae Geun Kim</b>

<img src="Fig/SM.PNG"></img>

### 1) Prepare Class (or Type)
* Make Particle class (or Type)
    * Default particle class has name, mass, charge, spin
* Make Fermion Class (or Type). If possible, inherit default particle class
* Make Boson Class (or Type). If possible, inherit default particle class
(Hint : Fermion - spin:half-integer, Boson - spin:integer)

### 2) Define Methods for Class (or Type)
* String (or ```__str__```) : Print(particle) -> Name: electron, Mass: blabla..
* Name : You can assign name for empty "Particle" class.
ex) ```var A Particle; A.Name="electron"``` or ```A = Particle(); A.Name="electron"```
* Charge : Same as Name
* Mass : Same as.
* Spin : Watch out! Boson allows only integer spin and Fermion allows only half integer spin.

### 3) Play with Instance
* Declare electron as instance of Fermion class and print this.
(Print(A) -> Name: "electron", Charge: -1, Mass: 0.51MeV, Spin: 1/2)
<br>

## 2.  