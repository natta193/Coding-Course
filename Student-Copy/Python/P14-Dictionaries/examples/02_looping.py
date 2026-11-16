stock = {"apples": 12, "pears": 0, "kiwis": 7}

for fruit in stock:              # keys
    print(fruit)

for qty in stock.values():       # values
    print(qty)

for fruit, qty in stock.items(): # both
    if qty == 0:
        print(f"Out of {fruit}!")
    else:
        print(f"{fruit}: {qty}")
