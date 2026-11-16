# A
for i in range(1, 11):
    if i % 3 == 0:
        print(i)

# B
word = input("Word: ")
rev = ""
for i in range(len(word) - 1, -1, -1):
    rev = rev + word[i]
print(rev)

# C
n = int(input("n: "))
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
