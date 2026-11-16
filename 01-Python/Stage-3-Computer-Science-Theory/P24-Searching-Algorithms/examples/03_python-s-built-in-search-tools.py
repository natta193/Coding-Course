import bisect

names = ["Ana", "Ben", "Cai", "Dev"]
print("Cai" in names)          # True  – linear search
print(names.index("Cai"))      # 2     – linear search
print("Cai" in set(names))     # True  – hashing, O(1)

scores = [12, 35, 47, 60, 88]   # sorted
i = bisect.bisect_left(scores, 50)
print(i)                       # 3 – where 50 would go
bisect.insort(scores, 50)      # insert, keeping it sorted
