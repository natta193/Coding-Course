bill = float(input("Total bill (£): "))
tip_percent = float(input("Tip %: "))
people = int(input("Number of people: "))

total = bill * (1 + tip_percent / 100)
each = total / people
print(f"Total with tip: £{total:.2f}")
print(f"Each person pays: £{each:.2f}")
