import matplotlib.pyplot as plt
import numpy as np

def f6_a(x, k):
    return (x + k) ** 2

k = [2, 4, 6, 8, 10, 12]
x = np.arange(-10, 10, 0.1)

for ki in k:
    y = []
    for xi in x:
        y.append(f6_a(xi, ki))
    plt.plot(x, y, label = "k =" + str(ki))

plt.title("Cau 6b")
plt.legend()
plt.show()