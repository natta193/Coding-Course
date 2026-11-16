data = [23, 8, 42, 15, 4, 16]
target = 15

biggest = data[0]
for x in data:
    if x > biggest:
        biggest = x

total = 0
for x in data:
    total += x

found = False
for x in data:
    if x == target:
        found = True

print("Max:", biggest, "Total:", total, "Found:", found)
