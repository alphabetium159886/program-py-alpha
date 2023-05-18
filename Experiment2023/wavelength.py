''' import numpy as np


def lambdaaa(x):
    return 390.922 + 0.0678 * x - 2.53 * 10 ** (-6) * x**2

a = np.array([508, 516, 1028, 1031, 1063])

print(lambdaaa(a))

#[424.71149808 425.23317232 457.94673648 458.13450867 460.13457843]
 '''
 
import numpy as np
import matplotlib.pyplot as plt
import sys
import io

# 读取数据
file_path = r"D:\Process-zone\experimentdata\0514-B.DAT"
data = np.loadtxt(file_path)

# 处理数据
# 计算峰值
peak_value = np.max(data)
peak_index = np.argmax(data)
peak_x = peak_index  # x轴为数据的索引

# 计算半高宽
half_max = peak_value / 2.0
left_index = np.where(data[:peak_index] < half_max)[0][-1]
right_indices = np.where(data[peak_index:] < half_max)[0]
if len(right_indices) > 0:
    right_index = right_indices[0] + peak_index
    half_width = right_index - left_index
else:
    half_width = np.nan  # 如果右侧没有低于半峰值的值，将半高宽设置为NaN

# 计算中心波长
central_wavelength = peak_x

# 绘制数据图形
plt.plot(data)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Data')
plt.show()

# 设置输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 输出计算结果
print("峰值：", peak_value)
print("半高宽：", half_width)
print("中心波长：", central_wavelength)

