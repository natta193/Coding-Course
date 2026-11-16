import random

def roll(sides=6):
    return random.randint(1, sides)

def roll_many(n, sides=6):
    return [roll(sides) for _ in range(n)]

counts = [0] * 13
for _ in range(10000):
    counts[roll() + roll()] += 1

for total in range(2, 13):
    bar = "#" * (counts[total] // 50)
    print(f"{total:2}: {bar} {counts[total]}")
# 7 is most common: 6 of the 36 combinations make 7
