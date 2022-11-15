import matplotlib.pyplot as plt
import numpy as np


def f7_a(x):
    return x ** 3 - (x / 2)

def f7_b(x):
    return x ** 2 + (x / 2)

def showFunc(x, y):
    plt.grid()
    plt.plot(x, y)
    plt.show()


#7a
x = np.arange(-10, 10, 0.1)
y = np.array(list(map(f7_a, x)))

plt.title('Cau 7a')
showFunc(x, y)
print("function f(x)_7a is one to one function")


#7b
x = np.arange(-10, 10, 0.1)
y = np.array(list(map(f7_b, x)))

plt.title('Cau 7b')
showFunc(x, y)
print("function f(x)_7b is not one to one function")