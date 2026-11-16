# TAKE-HOME PROJECT: Pattern Studio
# After lesson P06 (For Loops and range()) - about 1–2 hours, in chunks over the next few days.
#
# A menu program that draws patterns of any size, using nested for loops. Each pattern is
# a challenge in working out "how many spaces, how many stars on row r?".
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Menu: 1) square 2) right triangle 3) pyramid 4) diamond 5) checkerboard 6) quit –
#          keep showing the menu until they quit
#   [ ] 2. Ask for the size and the character to draw with
#   [ ] 3. Square and triangle first, then pyramid, then diamond (a pyramid + an upside-down
#          pyramid)
#   [ ] 4. Checkerboard: alternate the character and a space – use (row + col) % 2
#   [ ] 5. Put a blank line after each pattern
#
# Stretch: Add a hollow square, a times-table grid with columns lined up, and an "X"
# shape.
#
# Bring it to the next session - working or stuck, both are fine.

while True:
    print("1) square  2) triangle  3) pyramid  4) diamond  5) checkerboard  6) quit")
    choice = input("> ")
    if choice == "6":
        break
