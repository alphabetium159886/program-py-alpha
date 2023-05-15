import numpy as np
import matplotlib.pyplot as plt

def f(k, T, dE):
    return np.exp(-dE / (k * T))

def monte_carlo_ising_model(N, n, J, temperatures):
    B_array = np.zeros(len(temperatures))

    for k in range(len(temperatures)):
        T = temperatures[k]
        array = np.zeros(N)
        S = np.random.choice([-1, 1], size=(n, n))

        for i in range(N):
            index = np.random.randint(n, size=2)
            x1 = (index[0] - 1) % n
            x2 = index[0]
            x3 = (index[0] + 1) % n
            y1 = (index[1] - 1) % n
            y2 = index[1]
            y3 = (index[1] + 1) % n
            dE = 2 * J * S[x2, y2] * (S[x1, y2] + S[x3, y2] + S[x2, y1] + S[x2, y3])

            if dE > 0:
                a = np.random.rand()
                if a < f(1, T, dE):
                    S[x2, y2] = -1
            else:
                S[x2, y2] = -S[x2, y2]

            ss = np.sum(S) / (n * n)
            array[i] = ss

        plt.figure(1)
        plt.plot(array)
        array1 = array ** 2
        Sb = np.mean(array1[int(N * 3 / 10):])  # 平方和的平均值
        SSb = np.mean(array[int(N * 3 / 10):]) ** 2  # 平均值的平方
        answer = Sb - SSb  # 序参量的涨落
        B_array[k] = answer

    plt.figure(2)
    plt.plot(temperatures, B_array, 'ro-')
    plt.xlabel('Temperature')
    plt.ylabel('Fluctuation')
    plt.show()

N = 1000000  # 马尔科夫链长度
n = 100
J = 1
temperatures = np.linspace(1, 10, 10)  # 不同的温度

monte_carlo_ising_model(N, n, J, temperatures)
