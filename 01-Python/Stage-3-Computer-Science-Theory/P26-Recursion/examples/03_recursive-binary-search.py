def bsearch(items, target, low, high):
    if low > high:
        return -1                      # base case: not found
    mid = (low + high) // 2
    if items[mid] == target:
        return mid                     # base case: found
    if items[mid] < target:
        return bsearch(items, target, mid + 1, high)
    return bsearch(items, target, low, mid - 1)

nums = [2, 5, 8, 12, 16, 23, 38]
print(bsearch(nums, 16, 0, len(nums) - 1))   # 4
