import numpy as np
import matplotlib.pyplot as plt

data = np.array([49.04821, 49.05843, 49.0712, 49.08916, 49.11141, 49.12163, 49.1343, 49.15196])

# 生成对应的 x 值
x = np.arange(len(data))

# 一阶多项式拟合
coefficients = np.polyfit(x, data, 1)
fitted_curve = np.polyval(coefficients, x)

# 方差和标准差
variance = np.var(data)
std_deviation = np.std(data)

# 拟合曲线
plt.plot(x, data, 'bo-', label='dataset')
plt.plot(x, fitted_curve, 'r-', label='first order polynomial fitting')

# 方差和标准差
plt.text(0.5, 49.151, f"VAR(x): {variance:.4f}", ha='left', va='top')
plt.text(0.5, 49.148, f"Standard deviation: {std_deviation:.4f}", ha='left', va='top')

# 一阶多项式的具体表达式
text = f"first order polynomial fitting: {coefficients[1]:.4f} + {coefficients[0]:.4f}x"
plt.text(0.5, 49.145, text, ha='left', va='top')


plt.xlabel('dataset')
plt.ylabel('value')
plt.legend()
plt.legend(loc='lower right', bbox_to_anchor=(2.0, 0.0))
plt.show()
