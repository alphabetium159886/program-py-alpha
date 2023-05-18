import numpy as np
import matplotlib.pyplot as plt


file_paths = [
    r"D:\Process-zone\experimentdata\0514-r.DAT",
    r"D:\Process-zone\experimentdata\0514-y.DAT",
    r"D:\Process-zone\experimentdata\0514-B.DAT"
]

data = []
peak_values = []
central_wavelengths = []
half_widths = []

for file_path in file_paths:
    d = np.loadtxt(file_path)
    data.append(d)

    #峰值
    peak_value = np.max(d[:, 1])
    peak_values.append(peak_value)

    #中心波长
    central_wavelength = d[np.argmax(d[:, 1]), 0]
    central_wavelengths.append(central_wavelength)

    #半高宽
    half_max = peak_value / 2.0
    mask = d[:, 1] >= half_max
    indices = np.where(mask)[0]

    if len(indices) >= 2:
        left_index = indices[0]
        right_index = indices[-1]
        half_width = d[right_index, 0] - d[left_index, 0]
    else:
        half_width = np.nan

    half_widths.append(half_width)

#图形
colors = ['r', 'y', 'b']
labels = ['Red', 'Yellow', 'Blue']

plt.figure(figsize=(10, 6))
for i, d in enumerate(data):
    plt.plot(d[:, 0], d[:, 1], color=colors[i], label=labels[i])

    # 添加波峰、中心波长、半高宽和强度
    peak_value = peak_values[i]
    central_wavelength = central_wavelengths[i]
    half_width = half_widths[i]

    text = f"Peak: {peak_value:.2f}\nCenter Wavelength: {central_wavelength:.2f}\nHalf Width: {half_width:.2f}"
    plt.text(central_wavelength, peak_value, text, ha='center', va='bottom')

plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.title('Spectrum')
plt.legend()
plt.show()
