import turtle
t = turtle.Turtle()

def polygon(sides, length):
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)

polygon(3, 100)    # triangle
polygon(5, 80)     # pentagon
polygon(8, 50)     # octagon
turtle.done()
