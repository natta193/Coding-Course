import random
import time

def two_sum_slow(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
    return None

def two_sum_fast(nums, target):
    seen = set()
    for x in nums:
        if target - x in seen:
            return target - x, x
        seen.add(x)
    return None

nums = random.sample(range(1, 10_000_000), 3000)
target = -1          # impossible target = worst case for both
for fn in [two_sum_slow, two_sum_fast]:
    start = time.time()
    fn(nums, target)
    print(f"{fn.__name__}: {time.time() - start:.4f}s")
