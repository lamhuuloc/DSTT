from sympy import Symbol, factor
x = Symbol('x')
y = Symbol('y')
bieuthuc = x**3 - y**3
ket_qua = factor(bieuthuc) 
print(ket_qua)
from sympy import expand 
bieuthuc = (x - y)*(x**2 + x*y + y**2) 
ket_qua = expand(bieuthuc) 
print(ket_qua)