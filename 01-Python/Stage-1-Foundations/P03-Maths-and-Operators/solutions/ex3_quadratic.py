import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
disc = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(disc)) / (2 * a)
x2 = (-b - math.sqrt(disc)) / (2 * a)
print(f"x = {x1:.3f} or x = {x2:.3f}")
