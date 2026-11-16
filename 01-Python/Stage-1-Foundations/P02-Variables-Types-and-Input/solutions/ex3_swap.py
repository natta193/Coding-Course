a = 5
b = 9
# Method 1: temporary variable
temp = a
a = b
b = temp
print(a, b)   # 9 5

# Method 2: Python's tuple swap
a, b = b, a
print(a, b)   # back to 5 9

# Why a = b; b = a fails: after a = b, the original value of a is lost,
# so both end up as 9.
