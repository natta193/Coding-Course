def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def primes_up_to(n):
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
    return result

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

print(primes_up_to(50))
print(next_prime(100))   # 101
