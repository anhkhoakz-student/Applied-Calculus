import matplotlib.pyplot as plt
import math
import numpy as np

def f_1(x):
    return math.sqrt(1-(abs(x)-1)**2)

def f_2(x):
    return -3*math.sqrt(1-math.sqrt(abs(x)/2))

def draw_f_1():
    x_array = np.arange(-2, 2, 0.000001)
    y_array = list(map(f_1, x_array))
    plt.plot(x_array, y_array, color = 'magenta')

def draw_f_2():
    x_array = np.arange(-2, 2, 0.1)
    y_array = list(map(f_2, x_array))
    plt.plot(x_array, y_array, color = 'red')

draw_f_1()
draw_f_2()

plt.grid()
plt.show()