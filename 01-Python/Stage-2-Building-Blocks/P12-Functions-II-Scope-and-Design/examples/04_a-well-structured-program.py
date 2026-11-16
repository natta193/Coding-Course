def get_number(prompt, low, high):
    while True:
        n = int(input(prompt))
        if low <= n <= high:
            return n
        print(f"Must be {low}-{high}")

def times_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

def main():
    n = get_number("Which table? ", 1, 12)
    times_table(n)

if __name__ == "__main__":
    main()
