# ---- file: helpers.py ----
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Whole number please")

# ---- file: game.py (same folder) ----
import helpers

age = helpers.get_int("Age: ")
