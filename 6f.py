import matplotlib.pyplot as plt
import numpy as np

def f6_f(x):
    return (1/2)*(x+1) + 5

x = np.arange(-10, 10, 0.1)
y = np.array(f6_f(x))

plt.plot(x, y, label = 'base')
plt.plot(x - 1, y - 5, label = 'down 5, right 1')

plt.legend()
plt.title('Cau 6f')
plt.show()