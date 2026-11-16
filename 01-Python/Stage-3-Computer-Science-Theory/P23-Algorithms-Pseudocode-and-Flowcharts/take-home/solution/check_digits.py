def valid_isbn13(code):
    digits = [int(c) for c in code if c.isdigit()]
    if len(digits) != 13:
        return False
    total = sum(d * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))
    return total % 10 == 0


def make_isbn13(first12):
    digits = [int(c) for c in first12 if c.isdigit()]
    total = sum(d * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))
    return first12 + str((10 - total % 10) % 10)


def valid_luhn(number):
    digits = [int(c) for c in number if c.isdigit()]
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


print(valid_isbn13("978-0-306-40615-7"))   # True
print(valid_isbn13("978-0-306-40615-8"))   # False
print(make_isbn13("978030640615"))          # 9780306406157
print(valid_luhn("4539 1488 0343 6467"))    # True
print(valid_luhn("4539 1488 0343 6468"))    # False
# Trace (Luhn, last 4 digits 6467 reversed = 7,6,4,6): 7 → 7; 6×2=12-9=3; 4 → 4; 6×2=12-9=3 ...
