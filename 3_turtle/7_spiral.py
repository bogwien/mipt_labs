import turtle
import numpy as np

# Нарисуйте спираль.

turtle.shape('turtle')
turtle.speed(0)

alfa = 120

i = 1
while i <= 1000:
    angle = alfa / (np.pi * i / 10)
    turtle.forward(1)
    turtle.left(angle)
    i += 1

turtle.done()
