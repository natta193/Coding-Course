def add_binary(a, b):
    result = ""
    carry = 0
    for i in range(7, -1, -1):
        s = int(a[i]) + int(b[i]) + carry
        result = str(s % 2) + result
        carry = s // 2
    if carry:
        print("Overflow!")
    return result

print(add_binary("01101101", "01011001"))  # 11000110
print(add_binary("11001000", "01100100"))  # Overflow! 00101100
