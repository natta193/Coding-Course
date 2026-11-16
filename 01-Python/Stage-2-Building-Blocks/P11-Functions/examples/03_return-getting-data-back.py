def area(width, height):
    return width * height

def is_even(n):
    return n % 2 == 0

a = area(4, 5)
print(a)                       # 20
print(area(2, 3) + area(1, 1)) # 7
if is_even(10):
    print("10 is even")
