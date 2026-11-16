def to_binary(n, width=8):
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits.rjust(width, "0")

def to_denary(bits):
    total = 0
    for b in bits:
        total = total * 2 + int(b)
    return total

while True:
    c = input("1) den→bin 2) bin→den 3) den→hex 4) hex→den q) quit: ")
    if c == "q":
        break
    v = input("Value: ").strip()
    if c == "1":
        print(to_binary(int(v)))
    elif c == "2":
        print(to_denary(v))
    elif c == "3":
        print(hex(int(v))[2:].upper())
    elif c == "4":
        print(int(v, 16))
