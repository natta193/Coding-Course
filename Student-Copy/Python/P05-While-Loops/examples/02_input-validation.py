age = int(input("Age (1-120): "))

while age < 1 or age > 120:
    print("That's not a real age!")
    age = int(input("Age (1-120): "))

print(f"Thanks, you're {age}")
