import matplotlib.pyplot as plt
import numpy as np

def f7_a(x):
    return x ** 3 - (x / 2)

x = np.arange(-10, 10, 0.1)
y = np.array(list(map(f7_a, x)))

plt.plot(x, y)

plt.title('Cau 7a')
plt.show()
print("function f(x) is one to one function")