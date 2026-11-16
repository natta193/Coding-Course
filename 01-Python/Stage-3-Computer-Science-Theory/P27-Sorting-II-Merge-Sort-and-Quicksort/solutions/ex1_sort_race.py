import random
import time

def bubble(a):
    a = a[:]
    n = len(a)
    for p in range(n - 1):
        swapped = False
        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
    return a

def insertion(a):
    a = a[:]
    for i in range(1, len(a)):
        cur, j = a[i], i - 1
        while j >= 0 and a[j] > cur:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cur
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    l, r = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            out.append(l[i]); i += 1
        else:
            out.append(r[j]); j += 1
    return out + l[i:] + r[j:]

def quicksort(a):
    if len(a) <= 1:
        return a
    p = a[len(a) // 2]
    return quicksort([x for x in a if x < p]) + [x for x in a if x == p] + quicksort([x for x in a if x > p])

SORTS = {"bubble": bubble, "insertion": insertion, "merge": merge_sort, "quick": quicksort, "sorted()": sorted}
for n in [1000, 3000]:
    data = [random.random() for _ in range(n)]
    for name, fn in SORTS.items():
        start = time.time()
        assert fn(data) == sorted(data)
        print(f"n={n:>6}  {name:10} {time.time() - start:8.4f}s")
    print()
