import matplotlib.pyplot as plt
import numpy as np

def f6_d(x):
    return x ** 3

x = np.arange(1, 50, 0.1)
y = np.array(list(map(f6_d, x)))

plt.plot(x, y, label = 'base')
plt.plot(x + 1, y - 1, label = 'left 1, down 1')

plt.title('Cau 6d')
plt.legend()
plt.show()