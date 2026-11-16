def bubble_sort(items, key=lambda x: x, reverse=False):
    items = items[:]
    n = len(items)
    for p in range(n - 1):
        swapped = False
        for i in range(n - 1 - p):
            a, b = key(items[i]), key(items[i + 1])
            if (a < b) if reverse else (a > b):
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return items

print(bubble_sort([3, 9, 1, 7], reverse=True))
print(bubble_sort(["Bo", "Alexandra", "Sam", "Kim"], key=len))
print(bubble_sort([("Ana", 72), ("Ben", 91), ("Cai", 64)], key=lambda t: t[1], reverse=True))
