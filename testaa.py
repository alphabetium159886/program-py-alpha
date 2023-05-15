import numpy as np



eps = 8.85 * 10**(-12)
m = 9.1 * 10**(-31)
c = 3 * 10**8
e = 1.6 * 10**(-19)
lambda1 = np.array([351 * 10**(-9), 502 * 10**(-9), 10**(-6)])
B = 0.1
omega = c / (8 * 10**(-3))

''' 
print(eps * m * c**2/(e**2 * lambda1)) '''


deltak = (np.pi * c * omega**2 * m**2 * eps)/(B * e**3)

print(deltak)