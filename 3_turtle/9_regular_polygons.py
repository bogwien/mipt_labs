import turtle
import numpy as np

# Нарисуйте 10 вложенных правильных многоугольников


def draw_n_angle(angles, len):
    angle = 360 / angles

    turtle.left((180 - angle) / 2)
    for a in range(0, angles):
        turtle.left(angle)
        turtle.fd(len)
    turtle.right((180 - angle) / 2)


radius = 50

turtle.shape('turtle')
turtle.speed(0)

for n in range(3, 14):
    length = 2 * radius * np.sin(np.pi / n)
    radius += 25

    draw_n_angle(n, length)

    turtle.penup()
    turtle.forward(25)
    turtle.pendown()


turtle.done()
