import matplotlib.pyplot as plt
import numpy as np

def f6_e(x):
    return x ** (2/3)

x = np.arange(-10, 10, 0.1)
y = np.array(list(map(f6_e, x)))

plt.plot(x, y, label = 'base')
plt.plot(x-1, y-1, label = 'right 1, down 1')

plt.legend()
plt.title('Cau 6e')
plt.show()