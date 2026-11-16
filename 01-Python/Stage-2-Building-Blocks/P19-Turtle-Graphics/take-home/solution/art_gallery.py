import random
import turtle

screen = turtle.Screen()
t = turtle.Turtle(visible=False)
t.speed(0)


def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def star(size, colour):
    t.color(colour)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def night_sky():
    screen.bgcolor("midnightblue")
    for _ in range(60):
        move_to(random.randint(-350, 350), random.randint(-250, 280))
        star(random.randint(4, 18), random.choice(["white", "lightyellow", "lightblue"]))
    move_to(220, 120)
    t.color("lightyellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def spirograph():
    screen.bgcolor("black")
    colours = ["red", "orange", "yellow", "lime", "cyan", "violet"]
    move_to(0, 0)
    for i in range(72):
        t.color(colours[i % len(colours)])
        t.circle(120)
        t.left(5)


def skyline():
    screen.bgcolor("orange")
    x = -380
    while x < 380:
        w, h = random.randint(30, 80), random.randint(60, 300)
        move_to(x, -250)
        t.color("black")
        t.begin_fill()
        for side in [w, h, w, h]:
            t.forward(side)
            t.left(90)
        t.end_fill()
        for _ in range(h // 30):
            move_to(x + random.randint(5, max(6, w - 10)), -250 + random.randint(10, h - 10))
            t.color("yellow")
            t.dot(4)
        x += w + 2


ARTWORKS = {"1": night_sky, "2": spirograph, "3": skyline}
while True:
    choice = screen.textinput("Gallery", "1) night sky  2) spirograph  3) skyline  (blank = quit)")
    if not choice or choice not in ARTWORKS:
        break
    screen.clear()
    screen.tracer(0)
    t = turtle.Turtle(visible=False)
    t.speed(0)
    ARTWORKS[choice]()
    screen.update()
turtle.bye()
