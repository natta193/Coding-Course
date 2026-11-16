def bubble_sort(items):
    items = items[:]                  # don't change the original
    n = len(items)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break                     # already sorted!
    return items

print(bubble_sort([5, 1, 4, 2, 8]))
