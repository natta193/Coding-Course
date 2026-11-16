#  128  64  32  16   8   4   2   1
#    0   1   0   1   1   0   1   0   = 64+16+8+2 = 90

print(0b01011010)       # 90
print(bin(90))          # 0b1011010
print(int("1011010", 2))  # 90

for n in range(9):
    print(n, format(n, "04b"))
