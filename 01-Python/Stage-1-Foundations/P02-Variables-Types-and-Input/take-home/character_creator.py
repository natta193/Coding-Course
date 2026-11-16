# TAKE-HOME PROJECT: RPG Character Creator
# After lesson P02 (Variables, Types and Input) - about 1–2 hours, in chunks over the next few days.
#
# Build a character creator for an imaginary role-playing game. Ask the player questions,
# work out their stats with maths, and print a beautiful character sheet using f-strings.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Ask for a name, a class (warrior / mage / rogue – just type it for now) and age
#   [ ] 2. Ask for 3 numbers from 1–10: strength, smarts, speed. Store each in a variable
#   [ ] 3. Calculate: health = strength × 10 + 50, mana = smarts × 8, dodge chance = speed ×
#          3 (%)
#   [ ] 4. Print a character sheet with a border, lined-up labels and the calculated stats
#   [ ] 5. Add a "power level" = the average of the three stats, shown to 1 decimal place
#
# Stretch: Ask how many gold coins they start with and how much a sword costs; print how
# many swords they can buy and how much change is left (use // and %).
#
# Bring it to the next session - working or stuck, both are fine.

# RPG CHARACTER CREATOR
name = input("Character name: ")
