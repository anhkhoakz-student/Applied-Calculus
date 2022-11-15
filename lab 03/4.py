import matplotlib.pyplot as plt
import numpy as np
import math


def fx_4i(x):
    return -x**3

def fx_4j(x):
    return -1/(x**2)

def fx_4k(x):
    return -1/x

def fx_4l(x):
    return 1/abs(x)

def fx_4m(x):
    return math.sqrt(abs(x))

def fx_4n(x):
    return math.sqrt(abs(-x))

def showFunc(x_array, y_array):
    plt.plot(x_array, y_array)
    plt.grid()
    plt.show()


x_array = np.arange(-10, 10.1, 0.1)
y_array = list( map(fx_4i, x_array))
showFunc(x_array, y_array)
# print("4i, f(x) is decreasing as x-values belong to (-oo, +oo)")


x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4j, x_array))
showFunc(x_array, y_array)


x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4k, x_array))
showFunc(x_array, y_array)


x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4l, x_array))
showFunc(x_array, y_array)


x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4m, x_array))
showFunc(x_array, y_array)


x_array = np.arange(-10, 10.1, 0.1)
y_array = list(map(fx_4n, x_array))
showFunc(x_array, y_array)