def bubble_sort(items):
    items = items[:]
    n = len(items)
    for p in range(n - 1):
        for i in range(n - 1 - p):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items
