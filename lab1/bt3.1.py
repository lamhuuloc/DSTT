import numpy as np
vec1 = np.array([1., 3., 5.])
print("vec1 * 2 =", vec1 * 2)                   
print("vec1 * vec1 =", vec1 * vec1)             
print("vec1 / 2 =", vec1 / 2)
print("vec1 + vec1 =", vec1 + vec1)
try:
    vec2 = np.array([2., 4.])
    print("vec1 + vec2 =", vec1 + vec2)
except ValueError as e:
    print("vec1 + vec2 gây lỗi:", e)

vec3 = np.array([2., 4., 6.])
print("vec1 + vec3 =", vec1 + vec3)
print("vec1 / vec3 =", vec1 / vec3)
print("vec1 * vec3 =", vec1 * vec3)
print("2*vec1 + 5*vec3 =", 2*vec1 + 5*vec3)
# Truy xuất phần tử
print("vec3[2] =", vec3[2])

# Tạo vector với linspace
vec4 = np.linspace(0, 20, 5)
print("vec4 =", vec4)

# Vector toàn 0
vec5 = np.zeros(5)
print("vec5 =", vec5)

# Vector toàn 1
vec6 = np.ones(5)
print("vec6 =", vec6)

# Vector rỗng (giá trị không xác định)
vec7 = np.empty(5)
print("vec7 =", vec7)

# Vector ngẫu nhiên
print("Ngẫu nhiên với np.random.random:", np.random.random(5))

# Xử lý vector v
v = np.array([1., 3., 5.])
print("Tổng các phần tử v =", np.sum(v))
print("Số chiều vector v =", v.shape)

# Chuyển vị
print("v.transpose() =", v.transpose())

# Lấy một phần vector
v1 = v[:2]
print("v1 = v[:2] =", v1)

# Thay đổi giá trị
v[0] = 5
print("Sau khi v[0] = 5, v =", v)
print("v1 (bị ảnh hưởng) =", v1)

# Gán quá số phần tử sẽ gây lỗi
try:
    v1[:2] = [1., 2., 3.]
except ValueError as e:
    print("Gán quá kích thước v1[:2] = [1.,2.,3.] gây lỗi:", e)

# Gán lại giá trị hợp lệ
v1[:2] = [1., 2.]
print("v sau khi gán lại v1[:2] = [1., 2.] =", v)

# Biểu thức kết hợp
v3 = 2 * v[:2] + v1 * 3
print("v3 = 2 * v[:2] + v1 * 3 =", v3)

# Gán lại v1 là list mới
v1 = np.array([4, 6])
print("Sau khi v1 = [4, 6], v3 =", v3)
print("v vẫn giữ nguyên =", v)

# Một số phép toán khác
print("v + 10 =", v + 10.0)
print("np.sqrt(v) =", np.sqrt(v))
print("np.cos(v) =", np.cos(v))
print("np.sin(v) =", np.sin(v))

# Tích vô hướng (dot product)
print("np.dot(v1, v3) =", np.dot(v1, v3))
print("v1.dot(v3) =", v1.dot(v3))
print("v3.dot(v1) =", v3.dot(v1))

