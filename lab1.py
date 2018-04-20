import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import residue

X = np.array([[3, -1, 0, 0, 0, 0],
              [-1, 3, -1, 0, 0, 0],
              [0, -1, 3, -1, 0, 0],
              [0, 0, -1, 3, -1, 0],
              [0, 0, 0, -1, 3, -1],
              [0, 0, 0, 0, -1, 3]])

y = np.array([-1, 2, 2, -2, 2, 2])

solve = np.linalg.solve(X, y)
print(solve)
print(X @ solve)


fun = lambda x: (2.7 * x ** 2 + 3 * x + 3.7) / (6 * x ** 4 - 7 * x ** 2 + 2 * x + 12)
t = np.arange(start=-10, stop=10)
plt.plot(t, fun(t))
plt.xlabel('$X$')
plt.ylabel('$y$')
plt.title('$ \\frac{2.7x^2 + 3x + 3.7}{6x^4 - 7x^2 + 2x + 12}$')
plt.show()

ftt = np.fft.fft(fun(t))
plt.plot(t, np.real(ftt))
plt.plot(t, np.abs(ftt))
plt.plot(t, np.imag(ftt))
plt.legend(['real', 'abs', 'imag'])
plt.show()

up = np.poly1d([1, 0.652, 0.652, 1])
down = np.poly1d([1, -1.145, 0.727, -0.1205])
up_root = np.roots(up)
down_root = np.roots(down)
print(residue(down_root, up_root))

