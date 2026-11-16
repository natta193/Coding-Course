def mean(nums):
    return sum(nums) / len(nums)

def median(nums):
    s = sorted(nums)
    mid = len(s) // 2
    if len(s) % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2

def mode(nums):
    best, best_count = None, 0
    for n in nums:
        c = nums.count(n)
        if c > best_count:
            best, best_count = n, c
    return best

def range_of(nums):
    return max(nums) - min(nums)

data = [3, 7, 7, 2, 9, 4]
print(mean(data), median(data), mode(data), range_of(data))
print(median([5, 1, 3]))   # 3
