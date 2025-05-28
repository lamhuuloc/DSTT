from sympy import Symbol, sin, cos, simplify
x = Symbol('x') 
y = Symbol('y')
bieuthuc = x*x - x*y + y*y 
print(bieuthuc)
giatri = bieuthuc.subs({x:3, y:2}) 
print(giatri)
print("\nKiểm tra lại giá trị của x và y sau khi dùng subs:")
print("x =", x)
print("y =", y)
# Tình huống 1: Thay x = 3, y = x
giatri = bieuthuc.subs({x:3, y:x})
print("\nTình huống 1: Thay x = 3, y = x")
print("Kết quả:", giatri)
# Tình huống 2: Thay x = y, y = 3
giatri = bieuthuc.subs({x:y, y:3})
print("\nTình huống 2: Thay x = y, y = 3")
print("Kết quả:", giatri)
# Tình huống 3: Thay y = x, rồi x = 3
giatri = bieuthuc.subs({y:x}).subs({x:3})
print("\nTình huống 3: Thay y = x, rồi x = 3")
print("Kết quả:", giatri)

# Thay x = 1 - y và rút gọn
bieuthuc_moi = bieuthuc.subs({x:1 - y})
print("\nBiểu thức sau khi thay x = 1 - y:")
print("bieuthuc_moi =", bieuthuc_moi)

dongian = simplify(bieuthuc_moi)
print("Biểu thức sau khi rút gọn:")
print("dongian =", dongian)

# Ví dụ với biểu thức lượng giác
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print("\nBiểu thức lượng giác sau khi rút gọn:")
print("bt_moi =", bt_moi)

