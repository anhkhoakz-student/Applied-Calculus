import matplotlib.pyplot as plt
import numpy as np

def fx_4i(x):
    return -x**3

x_array = np.arange(-10, 10.1, 0.1)
y_array = list( map(fx_4i, x_array))

plt.plot(x_array, y_array)
plt.grid()
plt.show()

print("4i, f(x) is decreasing as x-values belong to (-oo, +oo)")