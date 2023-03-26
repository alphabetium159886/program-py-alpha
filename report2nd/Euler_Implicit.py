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
    e = y_num - y_exact(x)

    return x, e

def f(x, y):
    return x*y**2+2*y


x0 = 0
y0 = -5
a = 0
b = 5
h = 0.1
y = Euler_Implicit(f, y0, a, b, h)

x = np.linspace(a, b, len(y))
plt.plot(x, y, '-o',label='Numerical Solution')

x, e = error(f, y0, a, b, h)

plt.plot(x, e, '-o', label='Error')

plt.xlabel('x')
plt.title('Numerical Solution and Error')
plt.legend()
plt.show()


print(e)
