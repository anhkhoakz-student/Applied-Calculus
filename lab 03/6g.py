import matplotlib.pyplot as plt
import numpy as np

def f6_g(x):
    return 1/(x**2)

x = np.arange(-10, 10, 0.1)
y = np.array(f6_g(x))

plt.plot(x, y, label = 'base')
plt.plot(x + 2, y - 1, label = 'left 2, down 1')

plt.legend()
plt.title('Cau 6g')
plt.show()