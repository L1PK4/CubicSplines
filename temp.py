from spline import *
import numpy as np
import matplotlib.pyplot as plt

# f1 = np.cos
f1 = lambda x : np.sqrt(x)
x = np.linspace(0, np.pi, num=10)
y = f1(x)

b, c, d = solve(x, y)
def f(x0, i):
	return y[i] + b[i] * (x0 - x[i]) + c[i] * (x0 - x[i]) ** 2 + d[i] * (x0 - x[i]) ** 3

for i in range(9):
	xx = np.linspace(x[i], x[i + 1], num=10)
	yy = f(xx, i)
	plt.plot(xx, yy)
# x = np.linspace(0, np.pi, num=100)
# plt.plot(x, f1(x), color='red')

plt.show()