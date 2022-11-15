import matplotlib.pyplot as plt
import numpy as np

def f6_h(x):
    return 1 - (x**3)

x = np.arange(-10, 10, 0.1)
y = np.array(list(map(f6_h, x)))
y2 = np.array(list(map(f6_h, x/2)))


plt.plot(x, y, label = 'base')
plt.plot(x, y2, label = 'stretched horizontally by a factor of 2')

plt.legend()
plt.title('Cau 6h')
plt.show()