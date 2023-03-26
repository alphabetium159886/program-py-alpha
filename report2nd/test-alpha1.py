import numpy as np
import matplotlib.pyplot as plt


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


# 显式欧拉法
def Euler_Explicit(f, y0, a, b, h):
    n = round((b-a)/h)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(1, n+1):
        xi = a + i * h
        y[i] = y[i-1] + h * f(xi-1, y[i-1])

    return y


# 4th-order Runge-Kutta法
def RK4(f, y0, a, b, h):
    n = round((b-a)/h)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(1, n+1):
        xi = a + i * h
        k1 = h * f(xi-1, y[i-1])
        k2 = h * f(xi-1 + h/2, y[i-1] + k1/2)
        k3 = h * f(xi-1 + h/2, y[i-1] + k2/2)
        k4 = h * f(xi, y[i-1] + k3)
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return y


def error(f, y0, a, b, h, y_exact):
    y_num = f(f, y0, a, b, h)
    x = np.arange(a, b + h, h)[:-1]
    e = y_num - y_exact(x)

    return x, e


def f(x, y):
    return x*y**2+2*y

def error_implicit(f, y0, a, b, h):
    def y_exact(x):
        return 20*np.exp(2*x)/(np.exp(2*x) - 10*x*np.exp(2*x) - 9)
    
    y_num = Euler_Implicit(f, y0, a, b, h)
    x = np.arange(a, b + h, h)[:-1]
    e = y_num - y_exact(x[-1])
    
    return e[-1]

def error_explicit(f, y0, a, b, h):
    def y_exact(x):
        return 20*np.exp(2*x)/(np.exp(2*x) - 10*x*np.exp(2*x) - 9)
    
    y_num = Euler_Explicit(f, y0, a, b, h)
    x = np.arange(a, b + h, h)[:-1]
    e = y_num - y_exact(x[-1])
    
    return e[-1]

def error_RK4(f, y0, a, b, h):
    def y_exact(x):
        return 20*np.exp(2*x)/(np.exp(2*x) - 10*x*np.exp(2*x) - 9)
    
    y_num = RK4(f, y0, a, b, h)
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
step_sizes = np.arange(0.1, 0.2, 0.01)

for h in step_sizes:
    errors_implicit.append(error_implicit(f, y0, a, b, h))
    errors_explicit.append(error_explicit(f, y0, a, b, h))
    errors_RK4.append(error_RK4(f, y0, a, b, h))

# 绘制误差随着步长变化的收敛图形
plt.plot(step_sizes, errors_implicit, label='Implicit Euler')
#plt.plot(step_sizes, errors_explicit, label='Explicit Euler')
#plt.plot(step_sizes, errors_RK4, label='RK4')
plt.xlabel('Step Size')
plt.ylabel('Error at t=5')
plt.title('Convergence of ODE Solvers')
plt.legend()
plt.show()
