import math

print(round(2.5), round(3.5))   # 2 4  – "banker's rounding"
print(int(3.99))                # 3   – int() chops
print(math.floor(-2.5))         # -3  – always down
print(math.ceil(2.1))           # 3   – always up
print(round(7.456, 1))          # 7.5
print(17 // 5 * 5)              # 15  – round DOWN to a multiple of 5
