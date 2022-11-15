import matplotlib.pyplot as plt
import numpy as np

def fx_4i(x):
    return -x**3
def fx_4k(x):
    return  -1/x

#main

x_array = np.arange(-10, 10.1, 0.1)
y_array = list( map(fx_4i, x_array) )
plt.plot(x_array, y_array, color='red')
plt.grid()
plt.show()