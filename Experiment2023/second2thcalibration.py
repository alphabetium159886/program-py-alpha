import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')
# 标准波长和原胞数据
wavelength_std = np.array([404.66, 435.83, 546.07, 576.96, 579.07])
pixel_std = np.array([508, 516, 1028, 1031, 1063])

# 第一次校正中的二阶多项式系数
coefficients_1st = np.array([0.0678, -2.53e-6, 390.922])

# 第一次校正结果
wavelength_1st = np.polyval(coefficients_1st, pixel_std)

# 第二次二阶多项式拟合
coefficients_2nd = np.polyfit(pixel_std, wavelength_std - wavelength_1st, 2)

# 第二次校正测量波长
wavelength_measure_2nd = np.polyval(coefficients_2nd, pixel_std) + wavelength_1st

# 第二次校正测量误差
delta_lambda_2nd = wavelength_measure_2nd - wavelength_std

# 第二次校正相对误差
relative_error_2nd = delta_lambda_2nd / wavelength_std

print("第二次校正测量波长 (lambda):", wavelength_measure_2nd)
print("第二次校正测量误差 (Delta lambda):", delta_lambda_2nd)
print("第二次校正相对误差 (Delta lambda / lambda_0):", relative_error_2nd)
'''第二次校正测量波长 (lambda): [419.46266436 420.57152941 562.18512454 563.42485425 576.94582745]
第二次校正测量误差 (Delta lambda): [ 14.80266436 -15.25847059  16.11512454 -13.53514575  -2.12417255]
第二次校正相对误差 (Delta lambda / lambda_0): [ 0.0365805  -0.03501014  0.0295111  -0.02345942 -0.00366825]'''