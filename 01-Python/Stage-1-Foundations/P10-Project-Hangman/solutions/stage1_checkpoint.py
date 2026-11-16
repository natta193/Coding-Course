# 1
a = int(input("a: "))
b = int(input("b: "))
print(a + b, a - b, a * b)
# 2
n = int(input("n: "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
# 3
for i in range(20, -1, -4):
    print(i)
# 4
print(input("Word: ")[::-1])
# 5
count = 0
for ch in input("Sentence: "):
    if ch == "e":
        count += 1
print(count)
# 6
x = int(input("1-10: "))
while x < 1 or x > 10:
    x = int(input("1-10: "))
# 7
foods = ["pizza", "sushi", "tacos", "curry", "pasta"]
for i in range(len(foods)):
    print(i + 1, foods[i])
# 8
nums = [7, 3, 9, 1, 6]
smallest = nums[0]
for v in nums:
    if v < smallest:
        smallest = v
print(smallest)
# 9
for r in range(5):
    line = ""
    for c in range(5):
        line += "#"
    print(line)
# 10
for i in range(1, 51):
    if i % 7 == 0 or "7" in str(i):
        print(i)
