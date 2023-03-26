import numpy as np
import matplotlib.pyplot as plt


def Euler_Explicit(f, y0, h):
    t0 = 0
    tp = 1
    t = np.arange(t0, tp+h, h)
    y = np.zeros(len(t))
    y[0] = y0

    for i in range(0, len(t)-1):
        y[i+1] = y[i] + h * f((i+1) * h, y[i])
    return y

def error(f, y0, h):
    t0 = 0
    tp1 = 1
    
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
h = 0.1
y = Euler_Explicit(f, y0, h)
x, e = error(f, y0, h)
x = np.linspace(0, 5, len(y))
plt.plot(x, y, '-o',label='Numerical Solution')


plt.plot(x, e, '-o', label='Error')

plt.xlabel('x')
plt.title('Numerical Solution and Error')
plt.legend()
plt.show()


print(e)











