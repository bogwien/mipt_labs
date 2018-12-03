import turtle

# Нарисуйте 10 вложенных квадратов.

turtle.shape('turtle')
turtle.speed(0)

squareSize = 50
margin = 10

for squareNumber in range(1, 11):
    for lineNumber in range(1, 5):
        turtle.forward(squareSize)
        turtle.left(90)

    turtle.penup()
    turtle.goto(margin * squareNumber * -1, margin * squareNumber * -1)
    turtle.pendown()

    squareSize += margin * 2

turtle.done()
