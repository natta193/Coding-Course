def make_tea():
    sugar = 2              # local variable
    print(f"Tea with {sugar} sugars")

make_tea()
print(sugar)               # NameError!
