n = int(input("Start number: "))
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
    print(n)
print(f"Reached 1 in {steps} steps")
# Try 27 - it takes 111 steps and peaks at 9232!
