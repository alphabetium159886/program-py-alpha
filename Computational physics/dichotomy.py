import numpy as np
import matplotlib.pyplot as plt
import imageio

# 设置模拟参数
L = 1.0
nx = 128
ny = 128
dx = L / nx
dy = L / ny
dt = 0.1
nt = 200

# 创建初始磁场
Bx = np.zeros((nx, ny))
By = np.zeros((nx, ny))
Bx[64, :] = 1.0
By[:, 64] = -1.0

# 进行磁重联模拟
for i in range(nt):
    # 计算电场
    Ex = np.zeros((nx, ny))
    Ey = np.zeros((nx, ny))
    Ex[:, 1:-1] = (By[:, :-2] - By[:, 2:]) / (2 * dy)
    Ey[1:-1, :] = (Bx[:-2, :] - Bx[2:, :]) / (2 * dx)

    # 更新磁场
    Bx += dt * (-Ey)
    By += dt * Ex

    # 保存当前磁场图像
    plt.imshow(np.sqrt(Bx**2 + By**2), cmap='plasma')
    plt.axis('off')
    plt.savefig(f'frame_{i:04d}.png')
    plt.clf()

# 将图像序列合并为gif图像
images = []
for i in range(nt):
    images.append(imageio.imread(f'frame_{i:04d}.png'))
imageio.mimsave('magnetic_reconnection.gif', images)
