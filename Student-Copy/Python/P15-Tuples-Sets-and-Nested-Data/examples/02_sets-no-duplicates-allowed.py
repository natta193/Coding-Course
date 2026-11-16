tags = {"python", "games", "python", "maths"}
print(tags)          # {'games', 'maths', 'python'}

nums = [3, 1, 3, 2, 1]
print(set(nums))     # {1, 2, 3} – removes duplicates

a = {"Ana", "Ben", "Cai"}      # football club
b = {"Ben", "Dev", "Cai"}      # chess club
print(a | b)   # union: in either
print(a & b)   # intersection: in both
print(a - b)   # difference: football only
