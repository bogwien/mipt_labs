import turtle

# Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте функцию, рисующую звезду с n вершинами.


def draw_star(pet, len, points):
    deg = 180 + 180 / points

    if points == 5:
        pet.pen(pencolor="red", pensize=2)

    for step in range(0, points):
        pet.forward(len)
        pet.right(deg)

    pet.pen(pencolor="black", pensize=1)


turtle.shape('turtle')
turtle.speed(0)
pet1 = turtle.getturtle()

pet2 = pet1.clone()
pet2.penup()
pet2.goto(200, 0)
pet2.pendown()

draw_star(pet1, 150, 5)
draw_star(pet2, 150, 11)

turtle.done()
