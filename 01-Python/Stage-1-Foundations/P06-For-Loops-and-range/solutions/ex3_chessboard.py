size = int(input("Board size: "))
for row in range(size):
    line = ""
    for col in range(size):
        if (row + col) % 2 == 0:
            line += "  "
        else:
            line += "██"
    print(line)
