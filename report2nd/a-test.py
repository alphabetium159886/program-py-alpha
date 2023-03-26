import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 隐式欧拉法
def Euler_Implicit(f, y0, a, b, h):
    n = round((b-a)/h)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(1, n+1):
        xi = a + i * h
        yi = y[i - 1]
        for j in range(10):
            yi = y[i - 1] + h * f(xi, yi)
        y[i] = yi
    
    return y

def f(x, y):
    return x*y**2+2*y

def error_implicit(f, y0, a, b, h):
    def y_exact(x):
        return 20*np.exp(2*x)/(np.exp(2*x) - 10*x*np.exp(2*x) - 9)
    
    y_num = Euler_Implicit(f, y0, a, b, h)
    x = np.arange(a, b + h, h)[:-1]
    e = y_num - y_exact(x[-1])
    
    return e[-1]

# 定义参数
x0 = 0
y0 = -5
a = 0
b = 5

# 计算每个方法的误差
errors_implicit = []
errors_explicit = []
errors_RK4 = []
step_sizes = np.arange(0.1, 0.3, 0.01)

for h in step_sizes:
    errors_implicit.append(error_implicit(f, y0, a, b, h))

# 对数拟合函数
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# 对自变量（步长）和因变量（误差）都取对数
log_step_sizes = np.log(step_sizes)
log_errors_implicit = np.log(errors_implicit)

# 线性拟合
popt, pcov = curve_fit(func, log_step_sizes, log_errors_implicit)

# 画图
plt.plot(log_step_sizes, log_errors_implicit, 'bo', label='Error')
plt.plot(log_step_sizes, func(log_step_sizes, *popt), 'r-', label='Fit')
plt.xlabel('log(Step Size)')
plt.ylabel('log(Error at t=5)')
plt.title('Convergence of ODE Solvers (Log Fit)')
plt.legend()
plt.show()
