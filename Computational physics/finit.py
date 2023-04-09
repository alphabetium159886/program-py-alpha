import numpy as np

# 定义网格和时间步长
dx = dy = 0.01
dt = 0.0001

# 定义网格大小
nx = ny = 25

# 定义常数
kappa = 0.835

# 初始化温度矩阵
T = np.zeros((nx, ny))

# 设定边界条件
T[0, :] = 75  # 左边界
T[-1, :] = 50  # 右边界
T[:, 0] = 0  # 下边界
T[:, -1] = 100  # 上边界

# 定义追赶法函数
def tridiagonal_solve(A, B, C, D):
    nf = len(D)  # number of equations
    ac, bc, cc, dc = map(np.array, (A, B, C, D))  # copy arrays
    for it in range(1, nf):
        mc = ac[it-1]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1]
        dc[it] = dc[it] - mc*dc[it-1]

    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for il in range(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    del bc, cc, dc  # delete variables
    return xc

# 迭代求解
for n in range(1000):
    # 按照 x 方向求解
    Ax = kappa * dt / dx**2
    Bx = 1 + 2 * Ax
    Cx = Ax
    Dx = np.zeros((nx, ny))
    for j in range(1, ny-1):
        # 定义追赶法中的系数矩阵
        a = np.zeros(nx-2)
        b = np.zeros(nx-1)
        c = np.zeros(nx-2)
        d = np.zeros(nx-1)
        for i in range(1, nx-1):
            d[i-1] = T[i, j] + kappa * dt / dy**2 * (T[i, j-1] - 2 * T[i, j] + T[i, j+1])
            if i > 1:
                a[i-2] = -Ax
            b[i-1] = Bx
            if i < nx-1:
                c[i-1] = -Ax
        # 使用追赶法求解一维方程
        Tx = tridiagonal_solve(a, b, c, d)
        T[1:-1, j-1] = Tx

    # 按照 y 方向求解
    Ay = kappa * dt / dy**2
    By = 1 + 2 * Ay
    Cy = Ay
    Dy = np.zeros((nx, ny))
    for i in range(1, nx-1):
        # 定义追赶法中的系数矩阵
        a = np.zeros(ny-2)
        b    = np.zeros(ny-1)
    c = np.zeros(ny-2)
    d = np.zeros(ny-1)
    for j in range(1, ny-1):
        d[j-1] = T[i, j] + kappa * dt / dx**2 * (T[i-1, j] - 2 * T[i, j] + T[i+1, j])
        if j > 1:
            a[j-2] = -Ay
        b[j-1] = By
        if j < ny-1:
            c[j-1] = -Ay
    # 使用追赶法求解一维方程
    Ty = tridiagonal_solve(a, b, c, d)
    T[i, 1:-1] = Ty
print(T)
