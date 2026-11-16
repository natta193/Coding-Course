import turtle
t = turtle.Turtle()
t.left(90)
t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()

def tree(length):
    if length < 5:
        return
    t.pensize(max(1, length / 10))
    t.color("saddlebrown" if length > 20 else "forestgreen")
    t.forward(length)
    t.left(25)
    tree(length * 0.72)
    t.right(50)
    tree(length * 0.72)
    t.left(25)
    t.backward(length)

tree(100)
turtle.done()
