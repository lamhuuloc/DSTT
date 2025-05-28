import numpy as np
M1 = np.array([[9, 12], [23, 30]])
u = np.array([2, 1])
tichM1u = M1.dot(u)
tichuM1 = u.dot(M1)
dot_M1_u = np.dot(M1, u)
dot_u_M1 = np.dot(u, M1)
mat1 = np.zeros([5, 5])
mat2 = np.ones([5, 5])
mat3 = mat1 + 2 * mat2
mat4 = mat3
mat3[3][2] = 10
mat5 = np.copy(mat3)
mat6 = np.empty([4, 5])
mat7 = np.identity(4)
mat8 = np.random.random([4, 5])
(M1, u, tichM1u, tichuM1, dot_M1_u, dot_u_M1, mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8)