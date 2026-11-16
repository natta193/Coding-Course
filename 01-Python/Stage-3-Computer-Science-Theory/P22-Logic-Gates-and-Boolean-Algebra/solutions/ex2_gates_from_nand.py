def nand(a, b):
    return int(not (a and b))

def not_(a):
    return nand(a, a)

def and_(a, b):
    return not_(nand(a, b))

def or_(a, b):
    return nand(not_(a), not_(b))

def xor(a, b):
    n = nand(a, b)
    return nand(nand(a, n), nand(b, n))

for a in [0, 1]:
    for b in [0, 1]:
        assert and_(a, b) == (a & b)
        assert or_(a, b) == (a | b)
        assert xor(a, b) == (a ^ b)
    assert not_(a) == 1 - a
print("All gates work!")
