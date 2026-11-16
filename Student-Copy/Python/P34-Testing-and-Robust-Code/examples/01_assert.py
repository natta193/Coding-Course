def average(nums):
    assert len(nums) > 0, "average of empty list"
    return sum(nums) / len(nums)

assert average([2, 4]) == 3
assert average([5]) == 5
print("All good")
average([])     # AssertionError: average of empty list
