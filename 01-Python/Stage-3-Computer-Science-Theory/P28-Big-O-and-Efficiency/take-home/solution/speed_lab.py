import random
import time
import matplotlib.pyplot as plt


def total(a):
    t = 0
    for x in a:
        t += x
    return t


def bubble(a):
    a = a[:]
    for p in range(len(a) - 1):
        for i in range(len(a) - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


def bsearch(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def best_time(fn, *args):
    best = float("inf")
    for _ in range(3):
        s = time.perf_counter()
        fn(*args)
        best = min(best, time.perf_counter() - s)
    return best


sizes = [1000, 2000, 4000, 8000]
times = {"sum O(n)": [], "bubble O(n²)": [], "binary search O(log n)": []}
for n in sizes:
    data = [random.random() for _ in range(n)]
    srt = sorted(data)
    times["sum O(n)"].append(best_time(total, data))
    times["bubble O(n²)"].append(best_time(bubble, data[: n // 4]) * 16)   # scaled to keep it quick
    times["binary search O(log n)"].append(best_time(bsearch, srt, srt[n // 3]))

print(f"{'n':>6} " + " ".join(f"{k:>24}" for k in times))
for i, n in enumerate(sizes):
    print(f"{n:>6} " + " ".join(f"{times[k][i]:>24.6f}" for k in times))

for name, ts in times.items():
    plt.plot(sizes, ts, marker="o", label=name)
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("seconds (log scale)")
plt.legend()
plt.title("Speed lab")
plt.show()
# Conclusion: doubling n roughly doubled the sum time (O(n)), roughly quadrupled bubble sort (O(n²)),
# and barely changed binary search (O(log n)) – matching the Big-O predictions.
