import numpy as np
import matplotlib.pyplot as plt

# 定义模拟参数
L = 2*np.pi    # 空间范围
N = 100        # 离散化点数
dx = L/N       # 空间步长
dt = 0.01      # 时间步长
T = 5          # 总模拟时间

# 初始化速度场
x = np.linspace(0, L, N+1)
u = np.where(x < L/2, np.sin(x), -np.sin(x)) + 0.5*np.sin(2*x)

# 模拟时间演化
for t in np.arange(0, T, dt):
    # 计算速度场梯度
    du_dx = np.gradient(u, dx)

    # 更新速度场
    u += -du_dx * dt

# 绘制结果
plt.plot(x, u, color='b')
plt.xlabel('x')
plt.ylabel('u')
plt.title('Kelvin-Helmholtz Instability')
plt.show()
