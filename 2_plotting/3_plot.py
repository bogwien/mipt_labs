import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1000.01, 0.01)


def calculate_expression(value):
    return np.log((value**value + 1)**(- np.absolute(value) / 10), (1 + np.sin(value)**2)**-1)


plt.subplot(221)
plt.plot(x, calculate_expression(x))
plt.title(r'$f(x)$')
plt.grid(True)

plt.show()
