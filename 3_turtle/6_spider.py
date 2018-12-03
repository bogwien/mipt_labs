import turtle

# Нарисуйте паука с n лапами. Пример n = 12:

turtle.shape('turtle')
turtle.speed(0)

legs = 12
legLen = 100
angle = 360 / legs

for leg in range(1, legs + 1):
    turtle.forward(legLen)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(legLen)
    turtle.left(180 + angle)

turtle.done()
