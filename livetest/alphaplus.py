import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
# 定义常量
kappa = 0.835    
T_top = 100.0  
T_bottom = 0.0 
T_left = 75.0  
T_right = 50.0 
size = 100     
dx = 1         
dy = 1         
dt = 0.01      
steps = 1000   

# 初始化网格
T = np.zeros((size, size))

# 设置边界条件
T[:, 0] = T_left
T[:, -1] = T_right
T[0, :] = T_top
T[-1, :] = T_bottom

# 用中心有限差分计算下一个时间步长的温度
def evolve(T, kappa, dt, dx, dy):
    Tn = T.copy()
    Tn[1:-1, 1:-1] = T[1:-1, 1:-1] + kappa * dt * ((T[2:, 1:-1] - 2*T[1:-1, 1:-1] + T[:-2, 1:-1]) / dx**2 
                                                     + (T[1:-1, 2:] - 2*T[1:-1, 1:-1] + T[1:-1, :-2]) / dy**2)
    return Tn

# 创建动画
fig = plt.figure()
ims = []
for i in range(steps):
    # 计算下一个时间步长的温度
    T = evolve(T, kappa, dt, dx, dy)

    # 将温度网格添加到动画中
    im = plt.imshow(T, animated=True, cmap=plt.cm.hot)
    ims.append([im])

# 创建动画对象
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

# 显示动画并将其保存为gif
plt.show()
ani.save('temperature.gif', writer='imagemagick')
ani.save(os.path.join("C:/Users/toby1/Desktop", 'temperature.gif'), writer='imagemagick')
