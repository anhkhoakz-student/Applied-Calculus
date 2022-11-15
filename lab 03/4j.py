import matplotlib.pyplot as plt
import numpy as np

def fx_4j(x):
    return -1/(x**2)

x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4j, x_array))

plt.plot(x_array, y_array)
plt.grid()
plt.show()