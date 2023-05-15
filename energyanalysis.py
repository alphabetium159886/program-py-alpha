import re
import pandas as pd
import matplotlib.pyplot as plt
with open('D:\Process-zone\GROMACS-WORK\project-liquid\md.log', 'r') as file:
    content = file.read()

# 使用正则表达式提取能量数据
pattern = r'Energies \(kJ/mol\)\n(.*?\d+)\n\n'
energies_data = re.findall(pattern, content, re.DOTALL)

# 提取每个项的能量数据
energies_list = []
for data in energies_data:
    data_lines = data.strip().split('\n')[2:]
    energies = []
    for line in data_lines:
        if 'Step' not in line and 'Current' not in line and 'Total' not in line:
            values = line.split()
            energies.extend([float(value) for value in values])
    energies_list.append(energies)

df = pd.DataFrame(energies_list, columns=['LJ (SR)', 'Disper. corr.', 'Coulomb (SR)', 'Potential', 'Kinetic En.'])

# 打印DataFrame
print(df)

# 平均值、标准差
average_potential = df['Potential'].mean()
std_kinetic = df['Kinetic En.'].std()
DAS = df['Disper. corr.'].std()
DAA = df['Disper. corr.'].mean()
CSS = df['Coulomb (SR)'].std()
CAA = df['Coulomb (SR)'].mean()
LJA = df['LJ (SR)'].mean()
LJS = df['LJ (SR)'].std()
print("Average Potential: ", average_potential)
print("Standard Deviation of Kinetic Energy: ", std_kinetic)
print("DisperAverage:", DAA)
print("DisperStandard Deviation:",DAS)
print("CoulombAverage:",CAA)
print("CoulombStandard Deviation:",CSS)
print("LJ (SR)Average:",LJA)
print("LJ (SR)Standard Deviation:",LJS)

# 能量随时间变化
plt.figure(figsize=(10, 6))
steps = range(len(df))
# 势能
plt.plot(steps, df['Potential'], label='Potential')
# 动能
plt.plot(steps, df['Kinetic En.'], label='Kinetic Energy')
# Disper. corr.
plt.plot(steps, df['Disper. corr.'], label='Disper. corr.')
# Coulomb (SR)
plt.plot(steps, df['Coulomb (SR)'], label='Coulomb (SR)')
# LJ (SR)
plt.plot(steps, df['LJ (SR)'], label='LJ (SR)')
plt.xlabel('Time Steps')
plt.ylabel('Energy (kJ/mol)')
plt.title('Energy vs Time')
plt.legend()
plt.show()

# 势能随时间变化
plt.figure(figsize=(10, 6))
plt.plot(steps, df['Potential'])
plt.xlabel('Time Steps')
plt.ylabel('Potential (kJ/mol)')
plt.title('Potential Energy vs Time')
plt.show()

# 动能随时间变化
plt.figure(figsize=(10, 6))
plt.plot(steps, df['Kinetic En.'])
plt.xlabel('Time Steps')
plt.ylabel('Kinetic Energy (kJ/mol)')
plt.title('Kinetic Energy vs Time')
plt.show()

# Disper. corr.随时间变化
plt.figure(figsize=(10, 6))
plt.plot(steps, df['Disper. corr.'])
plt.xlabel('Time Steps')
plt.ylabel('Disper. corr. (kJ/mol)')
plt.title('Disper. corr. Energy vs Time')
plt.show()

# Coulomb (SR)随时间变化
plt.figure(figsize=(10, 6))
plt.plot(steps, df['Coulomb (SR)'])
plt.xlabel('Time Steps')
plt.ylabel('Coulomb (SR) (kJ/mol)')
plt.title('Coulomb (SR) Energy vs Time')
plt.show()

# LJ (SR)随时间变化
plt.figure(figsize=(10, 6))
plt.plot(steps, df['LJ (SR)'])
plt.xlabel('Time Steps')
plt.ylabel('LJ (SR) (kJ/mol)')
plt.title('LJ (SR) Energy vs Time')
plt.show()

