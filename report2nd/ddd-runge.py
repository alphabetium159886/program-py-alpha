import numpy as np
import matplotlib.pyplot as plt

def Runge_Kutta4(f, t0, y0, tn, h):
    res = [y0]
    t = t0
    for i in range(int((tn-t0)/h)):
        k1 = f(t, res[-1])
        k2 = f(t + h / 2, res[-1] + h * k1 / 2)
        k3 = f(t + h / 2, res[-1] + h * k2 / 2)
        k4 = f(t + h, res[-1] + h * k3)
        y_next = res[-1] + h * (k1 + 2 * k2 + 2 * k3 + k4)/6
        res.append(y_next)
        t += h
    return res

def f(x, y):
    return x*y**2+2*y

def error(f, y0, t0, tn, h):

    def y_exact(t):
        return 20*np.exp(2*x)/(np.exp(2*x) - 10*x*np.exp(2*x) - 9)

    y_num = Runge_Kutta4(f, t0, y0, tn, h)
    t = np.arange(t0, tn + h, h)
    e = y_num - y_exact(t)

    return t, e

y0 = -5
t0 = 0
tn = 5
h = 0.1

result = Runge_Kutta4(f, t0, y0, tn, h)
x = np.linspace(0, 5, len(result))
plt.plot(x, result, '-o',label='Numerical Solution')

t, e = error(f, y0, t0, tn, h)

plt.plot(t, e, '-o', label='Error')

plt.xlabel('t')
plt.title('Numerical Solution and Error')
plt.legend()
plt.show()

