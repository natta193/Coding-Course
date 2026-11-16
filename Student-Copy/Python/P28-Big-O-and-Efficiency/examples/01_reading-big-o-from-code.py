def first(items):            # O(1)
    return items[0]

def total(items):            # O(n)
    t = 0
    for x in items:
        t += x
    return t

def has_duplicate(items):    # O(n²)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False
