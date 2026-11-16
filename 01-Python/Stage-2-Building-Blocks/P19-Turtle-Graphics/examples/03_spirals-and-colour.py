import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)                     # fastest
colours = ["red", "orange", "yellow",
           "green", "cyan", "violet"]

for i in range(180):
    t.color(colours[i % 6])
    t.forward(i * 2)
    t.left(59)

turtle.done()
