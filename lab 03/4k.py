import matplotlib.pyplot as plt
import numpy as np

def fx_4k(x):
    return -1/x

x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4k, x_array))

plt.plot(x_array, y_array)
plt.grid()
plt.show()
