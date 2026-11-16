def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

def count(items, x):
    if not items:
        return 0
    return (items[0] == x) + count(items[1:], x)

def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result

def binary(n):
    if n < 2:
        return str(n)
    return binary(n // 2) + str(n % 2)

print(digit_sum(4725), count([1, 2, 1, 1], 1))
print(flatten([1, [2, [3, 4]], 5]))
print(binary(90))   # 1011010
