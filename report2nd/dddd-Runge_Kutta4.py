import numpy as np
import matplotlib.pyplot as plt
#runge的误差分析
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
    y_exact = lambda t: y0 * np.exp((t-t0)*t)
    y_num = Runge_Kutta4(f, t0, y0, tn, h)
    t = np.linspace(t0, tn, len(y_num))
    e = y_num - y_exact(t)
    return t, e

y0 = -5
t0 = 0
tn = 5

hs = np.arange(0.1, 0.51, 0.01)
errorlist = []

for h in hs:
    t, e = error(f, y0, t0, tn, h)
    errorlist.append(min(e))
    print(h,errorlist[-1])
plt.plot(hs, errorlist, label='error')
plt.xlabel('Step size h')
plt.ylabel('Absolute error')
plt.legend()
plt.show()

