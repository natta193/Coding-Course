def insertion_sort(items):
    items = items[:]
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]   # shift right
            j -= 1
        items[j + 1] = current        # drop it in
    return items

print(insertion_sort([5, 1, 4, 2, 8]))
