import matplotlib.pyplot as plt
import numpy as np

filename1 = r'D:\\Process-zone\\GROMACS\\project-liquid\\rdf_solid.xvg'
filename2 = r'D:\\Process-zone\\GROMACS\\project-liquid\\rdf_liquid.xvg'

data1 = np.loadtxt(filename1, comments=['@', '#'])
data2 = np.loadtxt(filename2, comments=['@', '#'])

r1 = data1[:, 0]
g_r1 = data1[:, 1]

r2 = data2[:, 0]
g_r2 = data2[:, 1]

plt.plot(r1, g_r1, label='Solid')
plt.plot(r2, g_r2, label='Liquid')

plt.xlabel('r (nm)')
plt.ylabel('g(r)')
plt.title('Radial Distribution Function')
plt.legend()
plt.show()
