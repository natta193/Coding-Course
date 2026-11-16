while True:
    print("1) square  2) triangle  3) pyramid  4) diamond  5) checkerboard  6) quit")
    choice = input("> ").strip()
    if choice == "6":
        break
    if choice not in "12345" or choice == "":
        print("Pick 1-6")
        continue
    size = int(input("Size: "))
    ch = input("Character: ") or "*"

    if choice == "1":
        for r in range(size):
            print(ch * size)
    elif choice == "2":
        for r in range(1, size + 1):
            print(ch * r)
    elif choice == "3":
        for r in range(1, size + 1):
            print(" " * (size - r) + ch * (2 * r - 1))
    elif choice == "4":
        for r in list(range(1, size + 1)) + list(range(size - 1, 0, -1)):
            print(" " * (size - r) + ch * (2 * r - 1))
    elif choice == "5":
        for r in range(size):
            line = ""
            for c in range(size):
                line += ch if (r + c) % 2 == 0 else " "
            print(line)
    print()
