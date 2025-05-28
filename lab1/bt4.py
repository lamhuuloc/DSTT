from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5
nghiem = solve((pt1, pt2), dict=True)
print(nghiem)
nghiem_0 = nghiem[0]
print(pt1.subs({x: nghiem_0[x], y: nghiem_0[y]}))
print(pt2.subs({x: nghiem_0[x], y: nghiem_0[y]}))