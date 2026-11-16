from itertools import product

def truth_table(func, n):
    names = "ABCDEFGH"[:n]
    print(" ".join(names), "| Q")
    for inputs in product([0, 1], repeat=n):
        print(" ".join(map(str, inputs)), "|", int(func(*inputs)))
    print()

truth_table(lambda a, b: a and not b, 2)
truth_table(lambda d, s, p: (d and s) or p, 3)
truth_table(lambda a, b, c: (a ^ b) ^ c, 3)     # odd parity
