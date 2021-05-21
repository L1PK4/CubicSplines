from spline import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, num=10)
y = np.cos(x)

b, c, d = solve(x, y)

s = [(x[i], x[i+1], lambda x0 : y[i] + b[i] * (x0 - x[i]) + c[i] * (x0 - x[i]) ** 2 + d[i] * (x0 - x[i]) ** 3) for i in range(len(x) - 1)]

for i, j, f in s:
    xx = np.linspace(i, j, num=10)
    plt.plot(xx, f(xx))
plt.show()