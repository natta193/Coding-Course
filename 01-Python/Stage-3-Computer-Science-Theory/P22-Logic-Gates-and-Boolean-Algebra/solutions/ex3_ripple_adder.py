import random

def half_adder(a, b):
    return a ^ b, a & b          # sum, carry

def full_adder(a, b, cin):
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, cin)
    return s2, c1 | c2

def to_bits(n):
    return [(n >> i) & 1 for i in range(8)]     # least significant first

def from_bits(bits):
    return sum(b << i for i, b in enumerate(bits))

def add8(x, y):
    a, b = to_bits(x), to_bits(y)
    carry = 0
    out = []
    for i in range(8):
        s, carry = full_adder(a[i], b[i], carry)
        out.append(s)
    return from_bits(out), carry

for _ in range(100):
    x, y = random.randint(0, 255), random.randint(0, 255)
    result, overflow = add8(x, y)
    assert result == (x + y) % 256 and overflow == int(x + y > 255)
print("8-bit adder matches Python for 100 random sums")
