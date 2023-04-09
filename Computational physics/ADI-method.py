import numpy as np
import matplotlib.pyplot as plt

L = 0.25  
W = 0.25  
T = 1  
##net
Nx = 51  
Ny = 51  
Nt = 1000  # 时间步数
dx = L / (Nx - 1)  # 空间步长(x方向)
dy = W / (Ny - 1)  # 空间步长(y方向)
dt = T / Nt  # 时间步长
kappa = 0.835  

x = np.linspace(0, L, Nx)
y = np.linspace(0, W, Ny)
X, Y = np.meshgrid(x, y)
#初始分布
u0 = np.zeros((Nx, Ny))
#boundary condition
u0[:, 0] = 100 
u0[:, -1] = 0  
u0[0, :] = 75  
u0[-1, :] = 50  

# 计算常数
ax = kappa * dt / dx**2
ay = kappa * dt / dy**2
bx = 1 - 2*ax
by = 1 - 2*ay


def AD(u1, ax, ay, bx, by):
    Nx, Ny = u1.shape
    u0 = u1.copy()
    # x 
    for j in range(1, Ny-1):
        a = np.zeros((Nx-2, Nx-2))
        b = np.zeros(Nx-2)
        for i in range(1, Nx-1):
            a[i-1, i-1] = bx
            if i > 1:
                a[i-1, i-2] = ax
            if i < Nx-2:
                a[i-1, i] = ax
            b[i-1] = ay * u1[i, j-1] + (1 - 2*ay) * u1[i, j] + ay * u1[i, j+1]
        u0[1:-1, j] = np.linalg.solve(a, b)
    # y 
    for i in range(1, Nx-1):
        a = np.zeros((Ny-2, Ny-2))
        b = np.zeros(Ny-2)
        for j in range(1, Ny-1):
            a[j-1, j-1] = by
            if j > 1:
                a[j-1, j-2] = ay
            if j < Ny-2:
                a[j-1, j] = ay
            b[j-1] = ax * u0[i-1, j] + (1 - 2*ax) * u0[i, j] + ax * u0[i+1, j]
        u1[i, 1:-1] = np.linalg.solve(a, b)
    return u1

# 迭代求解
u = u0.copy()

plt.figure()
plt.pcolor(X, Y, u, cmap='coolwarm', shading='auto')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Temperature at t = 1s')
plt.show()
