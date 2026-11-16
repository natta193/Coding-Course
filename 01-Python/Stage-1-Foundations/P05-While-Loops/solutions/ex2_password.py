PASSWORD = "python123"
attempts = 0
granted = False

while attempts < 3 and not granted:
    guess = input("Password: ")
    attempts += 1
    if guess == PASSWORD:
        granted = True
    else:
        print(f"Wrong – {3 - attempts} attempts left")

if granted:
    print("Access granted")
else:
    print("Locked out")
