import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen")
t.pensize(3)

t.forward(100)
t.left(90)
t.forward(100)
t.penup()
t.goto(-150, 50)
t.pendown()
t.circle(40)

turtle.done()     # keep window open
