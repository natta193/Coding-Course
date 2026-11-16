# Trace for n = 6:
# i:      6   5    4    3    2   (stops when i = 1)
# result: 6   30  120  360  720
# It calculates the factorial n! = n × (n-1) × ... × 1

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(6))   # 720
