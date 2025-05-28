from sympy import Symbol, solve, sqrt
x = Symbol('x')
bieuthuc1 = x + 3 - 5
nghiem1 = solve(bieuthuc1)
print("Nghiệm của phương trình x + 3 = 5 là:", nghiem1)
bieuthuc2 = x**2 + 3 - 5
nghiem2 = solve(bieuthuc2)
print("Nghiệm của phương trình x^2 + 3 = 5 là:", nghiem2)
print("Nghiệm thứ nhất:", nghiem2[0])
print("Nghiệm thứ hai:", nghiem2[1])