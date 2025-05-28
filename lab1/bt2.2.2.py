from sympy import Symbol, pprint
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - 2*x*y + y**2
pprint(bieuthuc)
bieuthuc
from sympy import init_printing
init_printing(order='rev-lex')
from sympy import factor
bieuthuc1 = factor(bieuthuc)
pprint(bieuthuc1)