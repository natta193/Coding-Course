import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
t.pensize(3)
STEP = 10
COLOURS = {"1": "black", "2": "red", "3": "blue", "4": "green", "5": "orange"}

def move(heading):
    t.setheading(heading)
    t.forward(STEP)

def toggle_pen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

screen.onkey(lambda: move(90), "Up")
screen.onkey(lambda: move(270), "Down")
screen.onkey(lambda: move(180), "Left")
screen.onkey(lambda: move(0), "Right")
screen.onkey(toggle_pen, "space")
screen.onkey(t.clear, "c")
for key, colour in COLOURS.items():
    screen.onkey(lambda c=colour: t.color(c), key)

screen.listen()
turtle.done()
