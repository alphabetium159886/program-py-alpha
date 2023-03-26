import numpy as np
import matplotlib.pyplot as plt


def Euler_Explicit(f, y0, h):
    t0 = 0
    tp = 5
    t = np.arange(t0, tp+h, h)
    y = np.zeros(len(t))
    y[0] = y0

    for i in range(0, len(t)-1):
        y[i+1] = y[i] + h * f((i+1) * h, y[i])
    return y

def error(f, y0, h):
    t0 = 0
    tp1 = 5
    
    def y_exact(x):
        return 20*np.exp(2*x)/(np.exp(2*x) - 10*x*np.exp(2*x) - 9)

    y_num = Euler_Explicit(f, y0, h)
    x = np.arange(t0, tp1 + h, h)
    e = y_num - y_exact(x)

    return x, e


def f(x, y):
    return x*y**2+2*y
x0 = 0
y0 = -5

#处理误差---
error_list = []
ha = np.arange(0.26, 0.7, 0.01)
for h in np.arange(0.26, 0.7, 0.01):
    
    y = Euler_Explicit(f, y0, h)
    x, e = error(f, y0, h)
    x = np.linspace(0, 5, len(y))
    error_list.append(e[-1])
    print(h,e[-1])


plt.plot(ha, error_list)
plt.xlabel('h')
plt.ylabel('e[-1]')
plt.title('Error vs. Step Size')
plt.show() 
#---0.33000000000000007 0.006333234725431014














