import numpy as np


def nonlinear(F, J, x0, tol=1e-8, maxiter=100):
    x = np.array(x0,dtype = float)
    for i in range(maxiter):
        Jx = J(x)
        Fx = F(x)
        delta = np.linalg.solve(Jx, -Fx)
        x += delta
        if np.linalg.norm(delta) < tol:
            return x
    raise RuntimeError("This method can't execute")
def f(x):
    return np.array([3*x[0] - np.cos(x[1]*x[2]) - 1/2,
                     x[0]**2 - 81*(x[1]+0.1)**2 + np.sin(x[2]) + 1.06,
                     np.exp(-x[0]*x[1]) + 20*x[2] + (10*np.pi-3)/3])

def J(x):
    return np.array([[3, x[2]*np.sin(x[1]*x[2]), x[1]*np.sin(x[1]*x[2])],
                     [2*x[0], -162*(x[1]+0.1), np.cos(x[2])],
                     [-x[1]*np.exp(-x[0]*x[1]), -x[0]*np.exp(-x[0]*x[1]), 20]])
x0 = [0.1, 0.1, -0.1]  # initial guess
sol = nonlinear(f, J, x0)  # solve the system
print(sol)
