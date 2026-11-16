class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __str__(self):
        return f"({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))    # (4, 6)
print(Vector(1, 1) == Vector(1, 1))   # True
