import turtle

# Нарисуйте окружность

turtle.shape('turtle')
turtle.speed(0)

turtle.left(90)

for x in range(1, 361, 1):
    turtle.forward(1)
    turtle.left(1)

turtle.done()
