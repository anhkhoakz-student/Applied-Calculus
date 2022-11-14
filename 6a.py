import matplotlib.pyplot as plt
import math
import numpy as np

def f6_a(x, k):
    return x**2+k
    
def cau6a(x, k):
    k = np.arange(2, 4, 6, 8, 10, 12)
    x = np.arange(-10, 10, 0.1)

for ki in k:
    y = []
    for xi in x:
        y.append(...)
    plt.plot(x, y, label = "k=" + str(ki) )

plt.title("Cau 6a")
plt.legend()
plt.show()