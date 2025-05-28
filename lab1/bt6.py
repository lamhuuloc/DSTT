import numpy as np
nguy_co = np.array([
    [0, 1, 2, 4, 5],   
    [0, 1, 2, 3, 5],   
    [0, 2, 3, 5, 7],   
    [0, 1, 3, 5, 9],   
    [0, 2, 4, 7, 20] 
])
A = np.array([[4, 1, 0, 0, 1],
              [2, 0, 2, 2, 1],
              [0, 1, 1, 1, 2],
              [0, 0, 0, 2, 2],
              [3, 2, 0, 1, 1]])

B = np.array([[0, 1, 1, 0, 1],
              [0, 1, 2, 2, 0],
              [1, 2, 2, 0, 0],
              [0, 2, 2, 2, 2],
              [1, 1, 0, 1, 0]])

C = np.array([[0, 2, 1, 0, 1],
              [0, 1, 1, 2, 1],
              [0, 2, 3, 2, 0],
              [0, 2, 3, 1, 0],
              [0, 1, 2, 2, 1]])

D = np.array([[3, 0, 1, 1, 0],
              [0, 2, 1, 1, 0],
              [2, 1, 1, 2, 1],
              [1, 1, 0, 2, 1],
              [0, 1, 0, 1, 0]])

E = np.array([[0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]])
total_risk = (
    nguy_co[0, A] +  
    nguy_co[1, B] +  
    nguy_co[2, C] + 
    nguy_co[3, D] +  
    nguy_co[4, E]   
)
def kich_ban_a():
    mask = (nguy_co[4, E] == 0) & (total_risk <= 5)
    return np.argwhere(mask)
def kich_ban_b():
    mask = (nguy_co[3, D] == 0) & (nguy_co[4, E] == 0) & (total_risk <= 5)
    return np.argwhere(mask)
def kich_ban_c():
    mask = (nguy_co[0, A] == 0) & (nguy_co[3, D] == 0) & (total_risk <= 5)
    return np.argwhere(mask)
def kich_ban_d():
    mask = (nguy_co[0, A] == 0) & (nguy_co[1, B] == 0) & (nguy_co[2, C] == 0) & (nguy_co[3, D] == 0) & (total_risk <= 5)
    return np.argwhere(mask)
def kich_ban_e():
    mask = (nguy_co[4, E] == 0) & (total_risk <= 5)
    return np.argwhere(mask)
print("Kịch bản a (chiến dịch ngắn hạn):", kich_ban_a())
print("Kịch bản b (tập luyện):", kich_ban_b())
print("Kịch bản c (mùa khô):", kich_ban_c())
print("Kịch bản d (mùa mưa):", kich_ban_d())
print("Kịch bản e (3 tháng):", kich_ban_e())