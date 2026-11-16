scores = [12, 45, 7, 33]
names = ["Ana", "Ben", "Cai"]
mixed = [1, "two", 3.0, True]
empty = []

print(scores[0])      # 12
print(scores[-1])     # 33
print(len(names))     # 3
scores[2] = 99        # lists ARE mutable
print(scores)         # [12, 45, 99, 33]
print(scores[1:3])    # [45, 99]
