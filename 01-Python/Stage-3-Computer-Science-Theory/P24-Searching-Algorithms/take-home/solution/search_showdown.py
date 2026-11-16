import random
import time

users = [f"user{i:07d}" for i in range(1_000_000)]


def linear(items, target):
    for i, x in enumerate(items):
        if x == target:
            return i, i + 1
    return -1, len(items)


def binary(items, target):
    lo, hi, comps = 0, len(items) - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comps += 1
        if items[mid] == target:
            return mid, comps
        if items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comps


targets = random.sample(users, 20)
lin_time = bin_time = 0.0
print(f"{'username':12} {'linear':>9} {'binary':>7}")
for t in targets:
    s = time.perf_counter(); _, lc = linear(users, t); lin_time += time.perf_counter() - s
    s = time.perf_counter(); _, bc = binary(users, t); bin_time += time.perf_counter() - s
    print(f"{t:12} {lc:>9,} {bc:>7}")
print(f"Total time – linear {lin_time:.3f}s, binary {bin_time:.6f}s")

words = sorted(["apple", "banana", "cherry", "dragon", "eagle", "forest", "galaxy", "harbour",
                "island", "jungle", "kettle", "lemon", "mango", "number", "orange", "python"])
secret = random.choice(words)
print("\nI'm thinking of one of:", ", ".join(words))
for guesses in range(1, 20):
    g = input("Guess: ").strip().lower()
    if g == secret:
        print(f"Got it in {guesses}!")
        break
    print("Earlier in the alphabet" if secret < g else "Later in the alphabet")
