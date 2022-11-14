import numpy as np
import matplotlib.pyplot as plt


def fx_4l(x):
    return 1/abs(x)

x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4l, x_array))

plt.plot(x_array, y_array)
plt.grid()
plt.show()