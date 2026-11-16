def power(base, exp=2):
    return base ** exp

print(power(5))        # 25 – uses default
print(power(2, 10))    # 1024

def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([4, 9, 1, 7])
print(low, high)       # 1 9
