import numpy as np
import matplotlib.pyplot as plt


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


def error(f, y0, a, b, h):

    def y_exact(x):
        return 20*np.exp(2*x)/(np.exp(2*x) - 10*x*np.exp(2*x) - 9)

    y_num = Euler_Implicit(f, y0, a, b, h)
    x = np.arange(a, b + h, h)
    e = y_num - y_exact(x[:-1])

    return x[:-1], e


def f(x, y):
    return x*y**2+2*y


x0 = 0
y0 = -5
a = 0
b = 5
h = 0.1
y = Euler_Implicit(f, y0, a, b, h)

error_list = []
ha = np.arange(0.26, 0.7, 0.01)
for h in np.arange(0.26, 0.7, 0.01):
    
    y = Euler_Implicit(f, y0, a, b, h)
    x, e = error(f, y0, a, b, h)
    x = np.linspace(0, 5, len(y))
    error_list.append(e[-1])
    print(h,e[-1])


plt.plot(ha, error_list)
plt.xlabel('h')
plt.ylabel('e[-1]')
plt.title('Error vs. Step Size')
plt.show() 

