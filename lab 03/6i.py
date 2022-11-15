import matplotlib.pyplot as plt
import numpy as np
import math

def f6_i(x):
    return math.sqrt(x + 1)

x = np.arange(0, 20, 0.1)
y = np.array(list(map(f6_i, x)))
y2 = np.array(list(map(f6_i, x*4)))

plt.plot(x, y, label = 'base')
plt.plot(x, y2, label = 'compressed horizontally by a factor of 4')

plt.legend()
plt.title('Cau 6i')
plt.show()