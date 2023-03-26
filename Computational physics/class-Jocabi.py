import numpy as np

def Jacobi(A, b, x_0, eps , max_iter):
    n = len(A)
    x = x_0.copy()

    for i in range(max_iter):
        x1 = np.zeros(n)
        for j in range(n):
            a1 = np.dot(A[j,:j],x1[:j])
            a2 = np.dot(A[j, j+1:], x[j+1:])
            x1[j] = (b[j] - a1 - a2) / A[j, j]
        if np.linalg.norm(x1 - x, ord=np.inf) < eps:
            return x1
        x = x1
    return x

'''
    n = A.shape[0]  # dimension of the problem
    x = x_0.copy()  # make a copy of the initial approximation
    for k in range(max_iter):
        x1 = np.zeros_like(x)
        for i in range(n):
            a1 = np.dot(A[i, :i], x[:i])
            a2 = np.dot(A[i, i+1:], x[i+1:])
            x1[i] = (b[i] - a1 - a2) / A[i, i]
        if np.linalg.norm(x1 - x) < eps:
            break
        x = x1
    return x
'''
def Jacobi1(A,b,N,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = np.zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = np.diag(A)
    R = A - np.diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = (b - np.dot(R,x)) / D
    return x


A = np.array([[2, -1, 0, 0, 0, 0],
              [-1, 2, -1, 0, 0, 0],
              [0, -1, 2, -1, 0, 0],
              [0, 0, -1, 2, -1, 0],
              [0, 0, 0, -1, 2, -1],
              [0, 0, 0, 0, -1, 2]])
b = np.array([1,0,1,0,0,1])
x0 = np.zeros(6)
max_iter = 100
eps = 1e-8

x = Jacobi1(A,b,N=100,x=None)
print(x)
