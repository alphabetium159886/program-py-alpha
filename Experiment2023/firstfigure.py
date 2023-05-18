import numpy as np
import matplotlib.pyplot as plt

# 标准波长和原胞数据
wavelength_std = np.array([404.66, 435.83, 546.07, 576.96, 579.07])
pixel_std = np.array([508, 516, 1028, 1031, 1063])

# 第一次校正中的二阶多项式系数
coefficients_1st = np.array([0.0678, -2.53e-6, 390.922])

# 计算第一次校正的波长
wavelength_1st = np.polyval(coefficients_1st, pixel_std)

# 绘制汞光谱图
plt.plot(pixel_std, wavelength_1st, 'ro-', label='校正后波长')

# 标注中心波长及强度
for i in range(len(wavelength_std)):
    plt.text(pixel_std[i], wavelength_1st[i], f"{wavelength_std[i]} nm", ha='center', va='bottom')

# 设置坐标轴标签
plt.xlabel('像素值')
plt.ylabel('波长 (nm)')

# 添加图例
plt.legend()

# 显示图像
plt.show()
