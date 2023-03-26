import numpy as np

def gauss_seidel(A, b, x0, epsilon, max_iterations):
    n = len(A)
    x = x0.copy()

#https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method
    for i in range(max_iterations):
        x_new = np.zeros(n)
        for j in range(n):
            s1 = np.dot(A[j, :j], x_new[:j])#A[j, :j]:L matrix
            s2 = np.dot(A[j, j + 1:], x[j + 1:])#A[j, j + 1:]:U matrix
            x_new[j] = (b[j] - s1 - s2) / A[j, j]
        if np.allclose(x, x_new, rtol=epsilon):
            return x_new
        x = x_new
    return x
def gauss_seidel1(A, b, x0, max_iter=1000, eps=1e-8):

    n = A.shape[0]  # dimension of the problem
    x = x0.copy()  # make a copy of the initial approximation
    for k in range(max_iter):
        for i in range(n):
            a1 = np.dot(A[i, :i], x[:i])
            a2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - a1 - a2) / A[i, i]
        if np.linalg.norm(A @ x - b) < eps:
            break
    return x

def F(x):
    return np.array([3*x[0] - np.cos(x[1]*x[2])-1/2,x[0]**2-81*(x[1]+0.1)**2+np.sin(x[2])+1.06,np.exp(-x[0]*x[1])+20*x[2]+(10*np.pi-3)/3])


def J(x):
    return np.array([3,x[2]*np.sin(x[1]*x[2]),x[1]*np.sin(x[1]*x[2])],[2*x[0],162*(x[1]+0.1),np.cos(x[2])],[-x[1]*np.exp(x[0]*x[1]),-x[0]*np.exp(x[0]*x[1]),20])

A = np.array([[2, -1, 0, 0, 0, 0],
              [-1, 2, -1, 0, 0, 0],
              [0, -1, 2, -1, 0, 0],
              [0, 0, -1, 2, -1, 0],
              [0, 0, 0, -1, 2, -1],
              [0, 0, 0, 0, -1, 2]])
b = np.array([1,0,1,0,0,1])
x0 = np.zeros(6)
eps = 1e-6
max_iter = 100

x = gauss_seidel(A, b, x0, eps, max_iter)

print(x)
