def cocktail_sort(items):
    items = items[:]
    start, end = 0, len(items) - 1
    passes = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        end -= 1
        passes += 1
        if not swapped:
            break
        swapped = False
        for i in range(end, start, -1):
            if items[i - 1] > items[i]:
                items[i - 1], items[i] = items[i], items[i - 1]
                swapped = True
        start += 1
        passes += 1
    return items, passes

print(cocktail_sort([2, 3, 4, 5, 1]))   # sorted in 2 passes; bubble sort needs 4
