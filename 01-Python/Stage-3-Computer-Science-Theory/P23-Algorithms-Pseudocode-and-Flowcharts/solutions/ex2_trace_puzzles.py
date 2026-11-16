def m1(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s
# m1: sum of the digits. m1(4725) = 18

def m2(word):
    count = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    return count
# m2: counts pairs of doubled letters. m2("bookkeeper") = 3

def m3(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# m3: Euclid's algorithm – highest common factor. m3(48, 18) = 6
#  a  | b
#  48 | 18
#  18 | 12
#  12 | 6
#  6  | 0   -> return 6

print(m1(4725), m2("bookkeeper"), m3(48, 18))
