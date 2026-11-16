import random

# 1
def is_vowel(ch):
    return ch.lower() in "aeiou"

# 2
def smallest_largest(nums):
    lo = hi = nums[0]
    for n in nums:
        if n < lo:
            lo = n
        if n > hi:
            hi = n
    return lo, hi

# 3
try:
    n = int(input("Number: "))
except ValueError:
    print("Not a number")

# 4
counts = {}
for w in "a b a c b a".split():
    counts[w] = counts.get(w, 0) + 1
print(counts)

# 5
print(set([1, 2, 3]) & set([2, 3, 4]))

# 6
with open("out.txt", "w") as f:
    f.write("hello\nworld\n")
with open("out.txt") as f:
    print(f.read().upper())

# 7
print(random.choice(["rock", "paper", "scissors"]))

# 8 A local variable is created inside a function and only exists while it runs;
#   a global is created outside all functions and can be read everywhere.
print(is_vowel("E"), smallest_largest([4, 9, 1]))
