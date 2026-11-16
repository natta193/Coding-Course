# 1. 173 = 10101101 = AD
# 2. A B | Q
#    0 0 | 1
#    0 1 | 1
#    1 0 | 0
#    1 1 | 1
def linear_search(items, target):
    for i, x in enumerate(items):
        if x == target:
            return i
    return -1

def binary_search(items, target):
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# 5. [2, 6, 1, 8] -> [2, 1, 6, 8] -> [1, 2, 6, 8]
def sum_to(n):
    return 0 if n == 0 else n + sum_to(n - 1)

# 7. O(log n), O(n²), O(n log n), O(1)
stack = []
for w in "one two three four".split():
    stack.append(w)
out = []
while stack:
    out.append(stack.pop())
print(" ".join(out))
print(linear_search([4, 2, 7], 7), binary_search([1, 3, 5, 7], 5), sum_to(10))
