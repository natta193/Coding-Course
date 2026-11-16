import random

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

rects = [Rectangle(random.randint(1, 10), random.randint(1, 10)) for _ in range(5)]
for r in rects:
    print(r.width, r.height, r.area(), r.is_square())
biggest = max(rects, key=lambda r: r.area())
print("Biggest area:", biggest.area())
