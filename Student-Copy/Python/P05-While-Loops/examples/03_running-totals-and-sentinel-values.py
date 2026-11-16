total = 0
count = 0
num = int(input("Number (0 to stop): "))

while num != 0:
    total += num
    count += 1
    num = int(input("Number (0 to stop): "))

if count > 0:
    print(f"Total {total}, average {total / count:.2f}")
