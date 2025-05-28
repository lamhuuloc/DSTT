from sympy import Symbol, solve
x = Symbol('x')
ptb2 = x**2 + 9*x + 8
nghiem1 = solve(ptb2, dict=True)
print("Nghiệm của x^2 + 9x + 8 = 0 là:", nghiem1)
ptb2_phuc = x**2 + 1*x + 10
nghiem2 = solve(ptb2_phuc, dict=True)
print("Nghiệm của x^2 + x + 10 = 0 là:", nghiem2)