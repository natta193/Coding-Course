def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i          # found: return position
    return -1                 # not found

names = ["Zoe", "Ana", "Max", "Ben", "Cai"]
print(linear_search(names, "Ben"))   # 3
print(linear_search(names, "Dev"))   # -1
