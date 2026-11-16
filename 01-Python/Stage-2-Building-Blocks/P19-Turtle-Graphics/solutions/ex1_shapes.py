import turtle
t = turtle.Turtle()
t.speed(0)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def polygon(sides, length):
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)

def star(points, size):
    angle = 180 - 180 / points       # works for odd numbers of points
    for _ in range(points):
        t.forward(size)
        t.right(angle)

def flower(petals, radius=40):
    for _ in range(petals):
        for _ in range(2):           # one petal = two arcs
            t.circle(radius, 60)
            t.left(120)
        t.left(360 / petals)

for i, colour in enumerate(["red", "purple", "orange"]):
    move_to(-200 + i * 200, -50)
    t.color(colour)
    flower(8)
move_to(-50, 150)
t.color("gold")
star(5, 100)
turtle.done()
