import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

L = 25  
n = 50  
dx = L / (n - 1) 
kappa = 0.835  
sigma = 0.25  
dt = sigma * dx**2 / kappa  
T = np.zeros((n, n))  
T[0, :] = 100 
T[-1, :] = 0 
T[:, 0] = 75  
T[:, -1] = 50 

# 绘图总数
total_frames = 15

# 数值解
frame_count = 0  # 已绘制的图形数量
for j in range(int(6000)):  # 模拟时间 60 s
    for i in range(1, n-1):
        for k in range(1, n-1):
            T[i, k] += sigma * kappa * (T[i+1, k] - 2*T[i, k] + T[i-1, k] + T[i, k+1] - 2*T[i, k] + T[i, k-1])

    # 绘制温度分布的 3D 图形
    if j % 50 == 0 and frame_count < total_frames:  # 每隔 0.5 s 绘制一次，直到达到总数
        frame_count += 1
        x = np.linspace(0, L, n)
        y = np.linspace(0, L, n)
        X, Y = np.meshgrid(x, y)

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, T, cmap='viridis')
        ax.set_xlabel('x (cm)')
        ax.set_ylabel('y (cm)')
        ax.set_zlabel('Temperature (Celsius)')
        plt.show()

        if frame_count >= total_frames:
            break  # 停止循环
