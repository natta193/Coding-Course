import turtle, random

screen = turtle.Screen()
screen.setup(800, 500)
screen.tracer(0)                   # draw manually = fast
pen = turtle.Turtle(visible=False)

def draw(data, highlight=()):
    pen.clear()
    w = 760 / len(data)
    for i, h in enumerate(data):
        pen.color("red" if i in highlight else "steelblue")
        pen.penup(); pen.goto(-380 + i * w, -230); pen.pendown()
        pen.begin_fill()
        for side in [w - 2, h * 4, w - 2, h * 4]:
            pen.forward(side); pen.left(90)
        pen.end_fill()
    screen.update()

draw(random.sample(range(1, 101), 40))
turtle.done()
