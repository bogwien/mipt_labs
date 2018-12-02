import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

t = np.arange(-10, 10.01, 0.01)

line, = ax.plot(np.sin(2*t), np.cos(3*t))


def animate(i):
    line.set_xdata(np.sin(2*t + i / 1000))
    return line,


ani = animation.FuncAnimation(fig, animate, interval=1, blit=True)

plt.show()
