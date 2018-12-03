import turtle

# Нарисуйте «бабочку» из окружностей


def draw_circle(radius, direction):
    for step in range(0, 360):
        turtle.forward(radius / 10)

        if direction == 0:
            turtle.left(1)
        else:
            turtle.right(1)


turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)

for r in range(10, 31, 2):
    for d in [0, 1]:
        draw_circle(r, d)

turtle.done()
