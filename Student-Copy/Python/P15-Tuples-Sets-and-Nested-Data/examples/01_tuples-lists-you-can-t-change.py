point = (3, 7)
colour = (255, 128, 0)

x, y = point              # unpacking
print(x, y)               # 3 7

point[0] = 5              # TypeError – immutable!

def divide(a, b):
    return a // b, a % b  # returns a tuple

q, r = divide(17, 5)
