name = input("Character name: ")
role = input("Class (warrior/mage/rogue): ")
age = int(input("Age: "))

strength = int(input("Strength (1-10): "))
smarts = int(input("Smarts (1-10): "))
speed = int(input("Speed (1-10): "))

health = strength * 10 + 50
mana = smarts * 8
dodge = speed * 3
power = (strength + smarts + speed) / 3

gold = int(input("Starting gold: "))
sword_price = 15
swords = gold // sword_price
change = gold % sword_price

print()
print("╔══════════════════════════════╗")
print(f"  {name.upper()} the {role.title()}")
print("╠══════════════════════════════╣")
print(f"  Age:          {age}")
print(f"  Strength:     {strength}")
print(f"  Smarts:       {smarts}")
print(f"  Speed:        {speed}")
print(f"  Health:       {health}")
print(f"  Mana:         {mana}")
print(f"  Dodge chance: {dodge}%")
print(f"  Power level:  {power:.1f}")
print(f"  Can buy {swords} swords with {change} gold left over")
print("╚══════════════════════════════╝")
