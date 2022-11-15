import matplotlib.pyplot as plt
import numpy as np
import math

def f6_j(x):
    return math.sqrt(x + 1)

x = np.arange(0, 20, 0.1)
y = np.array(list(map(f6_j, x)))

plt.plot(x, y, label = 'base')
plt.plot(x, y*3, label = 'stretched vertically by a factor of 3')

plt.legend()
plt.title('Cau 6j')
plt.show()