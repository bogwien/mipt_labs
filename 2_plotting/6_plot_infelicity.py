import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]

plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()

for deg in range(1, 4):
    z = np.polyfit(x, y, deg)
    p_f = np.poly1d(z)

    approx_x = x.copy()
    approx_x.append(6)
    approx_x.append(7)

    plt.plot(approx_x, p_f(approx_x))

plt.show()
