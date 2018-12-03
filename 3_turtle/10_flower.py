import turtle

# Нарисуйте «цветок» из окружностей.


def draw_circle():
    for step in range(0, 360):
        turtle.forward(1)
        turtle.left(1)


turtle.shape('turtle')
turtle.speed(0)

for n in range(1, 7):
    draw_circle()
    turtle.left(360 / 6)

turtle.done()
