def m1(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

def m2(word):
    count = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    return count

def m3(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Trace first, then uncomment:
# print(m1(4725))
# print(m2("bookkeeper"))
# print(m3(48, 18))
