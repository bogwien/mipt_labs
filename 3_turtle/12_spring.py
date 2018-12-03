import turtle

# Нарисуйте пружину. Используйте функцию, рисующую дугу.


def draw_circle(forward, angle, deg):
    deg = int(round(deg / angle))
    for step in range(0, deg):
        turtle.forward(forward)
        turtle.right(angle)


turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

for r in range(1, 6):
    draw_circle(1, 1, 180)
    draw_circle(1, 10, 180)

turtle.done()
