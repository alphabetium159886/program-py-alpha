import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

L = 0.25  # 平板边长
dx = 0.01
dy = 0.01  # 网格步长
dt = 0.01  # 时间步长
kappa = 0.835  # 热扩散系数
T_ini = np.zeros((int(L/dx), int(L/dy)))  # 初始条件

T_ini[0, :] = 100  # 上
T_ini[-1, :] = 0  # 下
T_ini[:, 0] = 75  # 左
T_ini[:, -1] = 50  # 右

t_start = 0
t_end = 10
t_range = np.arange(t_start, t_end+dt, dt)

# 迭代
T = T_ini
for t in t_range:
    # 三对角方程
    a = kappa * dt / dx**2
    # ax = ay = r 这里只显示 a
    r = a
    m, n = T.shape
    A = np.zeros((m*n, m*n))
    b = np.zeros(m*n)
    for i in range(m):
        for j in range(n):
            idalpha = i*n + j
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                A[idalpha, idalpha] = 1
                b[idalpha] = T[i, j]
            else:
                A[idalpha, idalpha-n] = -r
                A[idalpha, idalpha-1] = -1
                A[idalpha, idalpha] = 2*(1+r)
                A[idalpha, idalpha+1] = -1
                A[idalpha, idalpha+n] = -1/r
                b[idalpha] = T[i-1, j]*r + T[i, j-1] + T[i, j+1] + T[i+1, j]/r

    # 温度分布
    T_new = np.linalg.solve(A, b).reshape(m, n)
    T = T_new

# 画图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(np.arange(0, L, dx), np.arange(0, L, dy))
ax.plot_surface(X, Y, T, cmap='coolwarm')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('Temperature (℃)')
ax.set_title('Temperature Distribution')
plt.show()
