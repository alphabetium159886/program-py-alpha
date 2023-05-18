import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')
# 标准波长（nm）
lambda_0 = np.array([404.66, 435.83, 546.07, 576.96, 579.07])

# 原胞长度
x = np.array([508, 516, 1028, 1031, 1063])

# 二阶多项式系数
a = 390.922
b = 0.0678
c = -2.53e-6

# 校正后的波长（lambda）
lambda_calibrated = a + b*x + c*x**2

# 校正测量误差（Delta lambda）
delta_lambda = lambda_calibrated - lambda_0

# 相对误差（Delta lambda / lambda_0）
relative_error = delta_lambda / lambda_0

print("校正测量误差 (Delta lambda):", delta_lambda)


print("相对误差 (Delta lambda / lambda_0):", relative_error)

'''校正测量误差 (Delta lambda): [  20.05149808  -10.59682768  -88.12326352 -118.82549133 -118.93542157]
相对误差 (Delta lambda / lambda_0): [ 0.04955147 -0.02431413 -0.16137723 -0.205951   -0.2053904 ]
'''