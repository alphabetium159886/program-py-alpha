import numpy as np
from scipy.optimize import fsolve

x0 = np.array([[1, 1, 1]])  # 二维数组
x0 = x0.flatten()  # 展平为一维数组
err = 1e-6 # 误差
maxIter = 100 # 最大迭代次数

for iter in range(maxIter):
    xNew = np.zeros_like(x) # 用于存储新解
    for i in range(len(x)):
        # 以下三行用于计算新解中第i个分量的值
        xi = np.delete(x, i) # xi表示除去x(i)的其它分量
        def f(y):
            x_i = np.delete(x, i-1) # 删除第 i 个分量
            return [2 * x[i] - xi[1] + 1/2 * np.sin(x[i] * xi[0]),
                    -xi[0] + 2 * x[i] - np.sqrt(2)/2 * np.sqrt(xi[0] + x[2]),
                    1/2 * np.exp(-x[i] * xi[0]) + x[2] - 1/2 * np.cos(2 * np.pi * x[i])]
        xNew[i] = fsolve(f, xNew[0:i], xtol=1e-9) # 调用fsolve求解
        
    if np.linalg.norm(xNew - x) < err: # 判断是否满足误差要求
        break
        
    x = xNew # 更新解

print(x)
