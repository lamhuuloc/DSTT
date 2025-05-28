from sympy import Symbol 
x = Symbol('x') 
f = x + x + x + 2
print(f)
a = Symbol('Noi') 
b = Symbol('Chim')
tong = 3*b + 7*a 
print(tong)

from sympy import Symbol 
x = Symbol('x') 
y = Symbol('y') 
s = x*y + y*x 
print(s)

p = x*(x+2*x) 
print(p)

p = (x+2)*(y+3)
print(p)

p = (x+2)*(y+3) + (x+2)*(x-3) 
print(p)

p = x*(-x+2*x-x) 
print(p)

p = (x+2)*(y+3)
p.expand()