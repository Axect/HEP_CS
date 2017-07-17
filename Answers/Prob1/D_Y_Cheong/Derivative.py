#%%

class Derivative:
  def __init__(self, f, h=10**(-5)):
      self.f = f
      self.h = float(h)

  def __call__(self, x):
    f,h = self.f, self.h
    return (f(x+h) - f(x))/h



from math import sin, cos, exp, log

df = Derivative(sin)
x = 0
print("d(sin, 0)=",df(x))

df = Derivative(cos)
x = 0
print("d(cos, 0)=",df(x))

df = Derivative(exp)
x = 0
print("d(exp, 0)=",df(x))


def y(x):
    return x**2

df = Derivative(y)
x = 0
print("d(x^2, 0)=",df(x))


df = Derivative(log)
x = 0
print("d(ln, 0)=",df(x))

