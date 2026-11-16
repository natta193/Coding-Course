import random

def bubble_counts(items):
    items = items[:]
    comps = swaps = 0
    n = len(items)
    for p in range(n - 1):
        swapped = False
        for i in range(n - 1 - p):
            comps += 1
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comps, swaps

def insertion_counts(items):
    items = items[:]
    comps = shifts = 0
    for i in range(1, len(items)):
        cur = items[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if items[j] <= cur:
                break
            items[j + 1] = items[j]
            shifts += 1
            j -= 1
        items[j + 1] = cur
    return comps, shifts

print(f"{'n':>5} {'data':>8} | {'bubble comps':>12} {'swaps':>8} | {'insert comps':>12} {'shifts':>8}")
for n in [100, 1000]:
    for label, data in [("random", random.sample(range(n), n)),
                        ("sorted", list(range(n))),
                        ("reversed", list(range(n, 0, -1)))]:
        bc, bs = bubble_counts(data)
        ic, is_ = insertion_counts(data)
        print(f"{n:>5} {label:>8} | {bc:>12,} {bs:>8,} | {ic:>12,} {is_:>8,}")
# 10x more items -> roughly 100x more work: that's O(n²)
