import matplotlib.pyplot as plt
import math
import numpy as np

def f6_c(x, k):
    return k * math.sqrt(x)

k = [1/3, 1, 3, 6]
x = np.arange(1, 50, 0.1)

for ki in k:
    y = []
    for xi in x:
        y.append(f6_c(xi, ki))
    plt.plot(x, y, label = 'k = ' + str(ki))

plt.title('Cau 6c')
plt.legend()
plt.show()
