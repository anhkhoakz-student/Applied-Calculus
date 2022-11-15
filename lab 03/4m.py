import matplotlib.pyplot as plt
import numpy as np
import math

def fx_4m(x):
    return math.sqrt(abs(x))

x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4m, x_array))

plt.plot(x_array, y_array)
plt.grid()
plt.show()