import random
import string
import sys
import time

sys.setrecursionlimit(10000)


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
    out.extend(l[i:]); out.extend(r[j:])
    return out


def quicksort(a):
    if len(a) <= 1:
        return a
    p = random.choice(a)
    return quicksort([x for x in a if x < p]) + [x for x in a if x == p] + quicksort([x for x in a if x > p])


with open("words.txt", "w") as f:
    for _ in range(200_000):
        f.write("".join(random.choices(string.ascii_lowercase[:8], k=random.randint(3, 8))) + "\n")

with open("words.txt") as f:
    words = [w.strip() for w in f]

results = {}
for name, fn in [("merge sort", merge_sort), ("quicksort", quicksort), ("sorted()", sorted)]:
    start = time.perf_counter()
    out = fn(words)
    results[name] = time.perf_counter() - start
    assert out == sorted(words)
for name, t in results.items():
    print(f"{name:11} {t:7.3f}s")

ordered = sorted(words)
runs = []
i = 0
while i < len(ordered):
    j = i
    while j < len(ordered) and ordered[j] == ordered[i]:
        j += 1
    runs.append((j - i, ordered[i]))
    i = j
runs.sort(reverse=True)
print("Most common:", runs[:10])

with open("sorted_words.txt", "w") as f:
    f.write("\n".join(ordered))
# Timsort finds already-sorted "runs" in real data and merges them, uses insertion sort on
# small chunks, and is written in C – so it's both smarter and much faster per step.
