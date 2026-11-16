import random

def linear_search(items, target):
    comps = 0
    for i, x in enumerate(items):
        comps += 1
        if x == target:
            return i, comps
    return -1, comps

def binary_search(items, target):
    low, high, comps = 0, len(items) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        comps += 1
        if items[mid] == target:
            return mid, comps
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comps

data = list(range(0, 2_000_000, 2))      # 1,000,000 sorted even numbers
targets = [random.choice(data) for _ in range(200)]

lin = sum(linear_search(data, t)[1] for t in targets) / len(targets)
bi = sum(binary_search(data, t)[1] for t in targets) / len(targets)
print(f"Linear: {lin:,.0f} comparisons on average")
print(f"Binary: {bi:.1f} comparisons on average")
