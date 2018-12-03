import numpy as np
import matplotlib.pyplot as plt

print('Input function:')
funcString = str(input())


def calculate_expression(x):
    return eval(funcString)


data = np.arange(-100, 100.01, 0.01)

plt.subplot(221)
plt.plot(data, calculate_expression(data))
plt.title(r'$f(x)$')
plt.grid(True)

plt.show()
