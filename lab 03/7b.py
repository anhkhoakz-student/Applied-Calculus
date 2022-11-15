import matplotlib.pyplot as plt
import numpy as np

def f7_b(x):
    return x ** 2 + (x / 2)

x = np.arange(-10, 10, 0.1)
y = np.array(list(map(f7_b, x)))

plt.plot(x, y)

plt.title('Cau 7b')
plt.show()
print("function f(x) is not one to one function")