import random
import time

def estimate_pi(darts):
    inside = 0
    for _ in range(darts):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / darts

for n in [1_000, 100_000, 1_000_000]:
    start = time.time()
    est = estimate_pi(n)
    print(f"{n:>9,} darts: π ≈ {est:.5f}  ({time.time() - start:.2f}s)")
