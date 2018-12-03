import numpy as np
import matplotlib.pyplot as plt

alfa = 3
beta = 0.9


def calculate_expression(val):
    sum = 0
    for n in range(0, 101):
        result = beta**n * np.cos(alfa**n * np.pi * val)
        sum += result

    return sum


x = np.arange(-2, 2.01, 0.01)
plt.plot(x, calculate_expression(x))
plt.title(r'$f(x)$')
plt.grid(True)

plt.show()
