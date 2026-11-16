def quicksort(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    smaller = [x for x in items if x < pivot]
    equal   = [x for x in items if x == pivot]
    bigger  = [x for x in items if x > pivot]
    return quicksort(smaller) + equal + quicksort(bigger)

print(quicksort([38, 27, 43, 3, 9, 82, 10]))
