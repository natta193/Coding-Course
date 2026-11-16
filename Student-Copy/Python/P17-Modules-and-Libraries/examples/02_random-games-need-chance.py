import random

print(random.randint(1, 6))         # dice
print(random.random())              # 0.0 to 1.0
print(random.choice(["R", "P", "S"]))
cards = list(range(1, 11))
random.shuffle(cards)               # in place
print(random.sample(cards, 3))      # 3 different
random.seed(42)                     # repeatable!
