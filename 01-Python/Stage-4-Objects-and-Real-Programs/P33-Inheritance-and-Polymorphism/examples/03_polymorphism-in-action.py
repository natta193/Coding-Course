class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2

shapes = [Circle(1), Square(3), Circle(2.5)]
for s in shapes:
    print(type(s).__name__, round(s.area(), 2))
print("Total:", sum(s.area() for s in shapes))
