import numpy as np
a = 1.5
b = 2
eps = 1e-5
err = 10


def f(x):
    return np.sin(x)-x**2/4

while err>eps:
    x = (a+b)/2
    if f(x)*f(a)<0:
        b = x
    else:
        a = x
    err = np.abs(f(x))
    

print(f(x),x)


















