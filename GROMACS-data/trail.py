import numpy as np
import matplotlib.pyplot as plt

filename = r'D:\\Process-zone\\GROMACS\\project-liquid\\rdf_solid.xvg'

data = []
with open(filename, 'r') as file:
    for line in file:
        if not line.startswith('@') and not line.startswith('#'):
            data.append([float(value) for value in line.split()])

data = np.array(data)

time = data[:, 0]
values = data[:, 1]

plt.plot(time, values)
plt.xlabel('r (nm)')
plt.ylabel('g(r)')
plt.title('radical distribution function solid')
plt.show()
