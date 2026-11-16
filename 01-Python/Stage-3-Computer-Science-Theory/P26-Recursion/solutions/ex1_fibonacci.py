import time

calls = 0
def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

memo = {}
def fib_memo(n):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

start = time.time()
print(fib(27), f"{calls:,} calls, {time.time() - start:.2f}s")
start = time.time()
print(fib_memo(27), f"{time.time() - start:.5f}s")
print(fib_memo(300))   # instant!
