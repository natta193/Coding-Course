import math
import random
import turtle

class Shape:
    def __init__(self, x, y, colour):
        self.x, self.y, self.colour = x, y, colour

    def area(self):
        raise NotImplementedError

    def draw(self, t):
        t.penup(); t.goto(self.x, self.y); t.setheading(0); t.pendown()
        t.color(self.colour)
        t.begin_fill()
        self.outline(t)
        t.end_fill()

class Circle(Shape):
    def __init__(self, x, y, colour, r):
        super().__init__(x, y, colour)
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def outline(self, t):
        t.circle(self.r)

class Rect(Shape):
    def __init__(self, x, y, colour, w, h):
        super().__init__(x, y, colour)
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
    def outline(self, t):
        for side in [self.w, self.h, self.w, self.h]:
            t.forward(side); t.left(90)

class Triangle(Shape):
    def __init__(self, x, y, colour, side):
        super().__init__(x, y, colour)
        self.side = side
    def area(self):
        return math.sqrt(3) / 4 * self.side ** 2
    def outline(self, t):
        for _ in range(3):
            t.forward(self.side); t.left(120)

def random_shape():
    x, y = random.randint(-300, 250), random.randint(-250, 200)
    c = random.choice(["tomato", "gold", "teal", "orchid", "skyblue"])
    kind = random.choice([Circle, Rect, Triangle])
    if kind is Circle:
        return Circle(x, y, c, random.randint(10, 50))
    if kind is Rect:
        return Rect(x, y, c, random.randint(20, 90), random.randint(20, 90))
    return Triangle(x, y, c, random.randint(30, 90))

t = turtle.Turtle(visible=False)
turtle.Screen().tracer(0)
shapes = [random_shape() for _ in range(20)]
for s in shapes:
    s.draw(t)
turtle.Screen().update()
print(f"Total area: {sum(s.area() for s in shapes):,.0f}")
turtle.done()
