import random

def partition(a, low, high):
    r = random.randint(low, high)        # random pivot avoids the sorted-data trap
    a[r], a[high] = a[high], a[r]
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i

def quicksort(a, low=0, high=None):
    if high is None:
        high = len(a) - 1
    if low < high:
        p = partition(a, low, high)
        quicksort(a, low, p - 1)
        quicksort(a, p + 1, high)

data = [random.randint(0, 99) for _ in range(20)]
quicksort(data)
print(data)

already = list(range(900))
quicksort(already)        # without the random pivot this recurses ~900 deep (n² and near the recursion limit)
print(already == sorted(already))
