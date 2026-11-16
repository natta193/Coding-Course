import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
disc = b ** 2 - 4 * a * c

if disc < 0:
    print("No real solutions")
elif disc == 0:
    print(f"One solution: x = {-b / (2 * a):.3f}")
else:
    x1 = (-b + math.sqrt(disc)) / (2 * a)
    x2 = (-b - math.sqrt(disc)) / (2 * a)
    print(f"x = {x1:.3f} or x = {x2:.3f}")
