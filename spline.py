import numpy as np
from algorithm import *
# deltax = x(i+1) - xi
# deltay = y(i+1) - yi

def solve(x, y, eps = 1e-5):
	size = len(x)
	deltax = np.diff(x)
	deltay = np.diff(y)
	a = []
	b = [1]
	c = []
	d = []
	for i in range(1, size - 1):
		a.append(deltax[i - 1])
		b.append(2 * (deltax[i - 1] + deltax[i]))
		c.append(deltax[i])
		d.append(3 * (deltay[i] / deltax[i] - deltay[i - 1] / deltax[i - 1]))
	b.append(1)
	c = algo(a, b, c, d)
	# print(np.shape(a), np.shape(b), np.shape(c), np.shape(d), size)
	d = np.zeros(shape = size-1)
	b = np.zeros(shape = size-1)
	for i in range(len(d)):
		d[i] = (c[i+1] - c[i]) / (3*deltax[i])
		b[i] = (deltay[i]/deltax[i]) - (deltax[i]/3)*(2*c[i] + c[i+1])  
	return b.squeeze(), c.squeeze(), d.squeeze() 