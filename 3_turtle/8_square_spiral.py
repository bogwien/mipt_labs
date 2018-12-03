import turtle

# Нарисуйте квадратную спираль.

turtle.shape('turtle')
turtle.speed(0)

i = 1
while i <= 300:
    turtle.forward(i * 2)
    turtle.left(90)
    i += 1

turtle.done()
