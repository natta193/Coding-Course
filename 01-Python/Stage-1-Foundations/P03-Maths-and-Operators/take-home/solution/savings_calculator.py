import math

item = input("What do you want to buy? ")
price = float(input("Price (£): "))
saved = float(input("Saved so far (£): "))
weekly = float(input("Weekly pocket money (£): "))

needed = max(0, price - saved)
weeks = math.ceil(needed / weekly)
months = weeks // 4
extra_weeks = weeks % 4

print(f"\nYou need £{needed:.2f} more for the {item}.")
print(f"That's {weeks} weeks of saving ({months} months and {extra_weeks} weeks).")

half_weeks = max(1, math.ceil(weeks / 2))
per_week_needed = needed / half_weeks
chores = math.ceil(max(0, per_week_needed - weekly) / 2)
print(f"To do it in {half_weeks} weeks, do {chores} chores (£2 each) per week.")
