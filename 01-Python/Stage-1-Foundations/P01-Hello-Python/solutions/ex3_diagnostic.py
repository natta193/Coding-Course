# 1
print(17 / 5)

# 2
name = input("What's your name? ")
print("Hello, " + name + "!")

# 3
n = int(input("Number: "))
if n > 100:
    print("Bigger than 100")
else:
    print("Not bigger than 100")

# 4
for i in range(1, 11):
    print(i)

# 5
total = 0
num = int(input("Number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Number (0 to stop): "))
print("Total:", total)
