import turtle

# Нарисуйте смайлик


def draw_circle(forward, angle, deg):
    deg = int(round(deg / angle)) if angle != 0 else 0
    for step in range(0, deg):
        turtle.forward(forward)
        turtle.right(angle)


turtle.shape('turtle')
turtle.speed(0)

turtle.fillcolor('yellow')
turtle.begin_fill()
draw_circle(1, 1, 360)
turtle.end_fill()
turtle.penup()
turtle.goto(-20, -30)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
draw_circle(1, 10, 360)
turtle.end_fill()
turtle.penup()
turtle.goto(20, -30)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
draw_circle(1, 10, 360)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()

draw_circle(1, 10, 180)
turtle.penup()
turtle.goto(15, -90)
turtle.pendown()

turtle.left(90)
turtle.pen(pencolor="red", pensize=3)
draw_circle(1, 5, 180)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.done()
