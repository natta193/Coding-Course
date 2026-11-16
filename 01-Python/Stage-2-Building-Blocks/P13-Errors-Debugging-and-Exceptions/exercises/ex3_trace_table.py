def mystery(n):
    result = 1
    i = n
    while i > 1:
        result = result * i
        i = i - 1
    return result

# Trace mystery(6) on paper first!
print(mystery(6))
