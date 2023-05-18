import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 标准波长和原胞数据
wavelength_std = np.array([404.66, 435.83, 546.07, 576.96, 579.07])
pixel_std = np.array([508, 516, 1028, 1031, 1063])

# 校正多项式系数
coefficients = np.polyfit(pixel_std, wavelength_std, 3)

# 测量波长及校正误差
pixel_measure = np.array([508, 516, 1028, 1031, 1063])
wavelength_measure = np.polyval(coefficients, pixel_measure)
delta_lambda = wavelength_measure - np.interp(pixel_measure, pixel_std, wavelength_std)
relative_error = delta_lambda / wavelength_measure

print("测量波长 (lambda):", wavelength_measure)
print("校正测量误差 (Delta lambda):", delta_lambda)
print("相对误差 (Delta lambda / lambda0):", relative_error)

'''测量波长 (lambda): [404.99275138 435.48178028 560.44292843 561.42083366 580.25170626]
校正测量误差 (Delta lambda): [  0.33275138  -0.34821972  14.37292843 -15.53916634   1.18170626]
相对误差 (Delta lambda / lambda0): [ 0.00082162 -0.00079962  0.02564566 -0.02767829  0.00203654]'''