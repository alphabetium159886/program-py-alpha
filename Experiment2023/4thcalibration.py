import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 标准波长和原胞数据
wavelength_std = np.array([404.66, 435.83, 546.07, 576.96, 579.07])
pixel_std = np.array([508, 516, 1028, 1031, 1063])

# 4阶多项式拟合
coefficients = np.polyfit(pixel_std, wavelength_std, 4)

# 测量波长
pixel_measure = np.array([508, 516, 1028, 1031, 1063])
wavelength_measure = np.polyval(coefficients, pixel_measure)

# 校正测量误差
delta_lambda = wavelength_measure - wavelength_std

# 相对误差
relative_error = delta_lambda / wavelength_std

print("测量波长 (lambda):", wavelength_measure)
print("校正测量误差 (Delta lambda):", delta_lambda)
print("相对误差 (Delta lambda / lambda_0):", relative_error)
'''测量波长 (lambda): [404.66 435.83 546.07 576.96 579.07]
校正测量误差 (Delta lambda): [ 4.98232566e-10  5.98390670e-10 -1.67688086e-10 -9.54969437e-11
 -8.66180017e-10]
相对误差 (Delta lambda / lambda_0): [ 1.23123750e-12  1.37299101e-12 -3.07081667e-13 -1.65517443e-13
 -1.49581228e-12]'''