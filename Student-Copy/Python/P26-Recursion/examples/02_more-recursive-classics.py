def total(nums):
    if not nums:
        return 0
    return nums[0] + total(nums[1:])

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

def countdown(n):
    if n == 0:
        print("Lift off!")
        return
    print(n)
    countdown(n - 1)

print(total([3, 4, 5]), power(2, 10))
countdown(3)
