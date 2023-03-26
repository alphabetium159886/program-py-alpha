import numpy as np
import matplotlib.pyplot as plt

#EE的误差分析
def Euler_Explicit(f, y0, h):
    t0 = 0
    tp = 5
    t = np.arange(t0, tp+h, h)
    y = np.zeros(len(t))
    y[0] = y0

    for i in range(0, len(t)-1):
        y[i+1] = y[i] + h * f((i+1) * h, y[i])
    return y

def error(f, y0, h):
    t0 = 0
    tp1 = 5
    
    def y_exact(x):
        return 20*np.exp(2*x)/(np.exp(2*x) - 10*x*np.exp(2*x) - 9)

    y_num = Euler_Explicit(f, y0, h)
    x = np.arange(t0, tp1 + h, h)
    e = y_num - y_exact(x)

    return x, e


def f(x, y):
    return x*y**2+2*y
x0 = 0
y0 = -5

#处理误差---
error_list = []
ha = np.arange(0.26, 0.41, 0.01)
for h in ha:
    y = Euler_Explicit(f, y0, h)
    x, e = error(f, y0, h)
    x = np.linspace(0, 5, len(y))
    error_list.append(e[-1])
    print(h,e[-1])


plt.plot(ha, error_list)
plt.xlabel('h')
plt.ylabel('e[-1]')
plt.title('Error vs. Step Size')
plt.show() 
#---0.33000000000000007 0.006333234725431014


fit = np.polyfit(ha, error_list, 1)
print("Slope of the fitted line (p):", fit[0])

plt.plot(ha, error_list, 'o', label='error')
plt.plot(ha, np.polyval(fit, ha), 'r--', label='fit')
plt.text(0.5, 0.9, f'Slope (k): {fit[0]:.4f}', ha='center', va='center', transform=plt.gca().transAxes)
plt.xlabel('log(h)')
plt.ylabel('log(Absolute error)')
plt.legend()
plt.show()









