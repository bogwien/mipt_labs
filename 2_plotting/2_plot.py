import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100, 100.01, 0.01)

plt.subplot(221)
plt.plot(x, x**2 - x - 6)
plt.title(r'$f(x)$')
plt.grid(True)

plt.show()
