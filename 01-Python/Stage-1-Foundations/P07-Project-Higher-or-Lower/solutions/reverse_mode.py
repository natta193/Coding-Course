low, high = 1, 100
tries = 0
print("Think of a number from 1 to 100...")

while True:
    guess = (low + high) // 2
    tries += 1
    reply = input(f"Is it {guess}? (h = too high, l = too low, c = correct) ").lower()
    if reply == "c":
        print(f"Got it in {tries} tries!")
        break
    elif reply == "h":
        high = guess - 1
    elif reply == "l":
        low = guess + 1
    if low > high:
        print("Hmm, you must have made a mistake somewhere!")
        break
