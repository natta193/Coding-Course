hero = {
    "name": "Ayla",
    "hp": 30,
    "gold": 10,
    "inventory": {"potion": {"qty": 2, "value": 5}},
}

def pick_up(char, item, value, qty=1):
    inv = char["inventory"]
    if item in inv:
        inv[item]["qty"] += qty
    else:
        inv[item] = {"qty": qty, "value": value}

def sell(char, item):
    inv = char["inventory"]
    if item not in inv:
        print(f"No {item} to sell")
        return
    char["gold"] += inv[item]["value"]
    inv[item]["qty"] -= 1
    if inv[item]["qty"] == 0:
        del inv[item]

def show(char):
    print(f"{char['name']} – HP {char['hp']} – {char['gold']} gold")
    items = sorted(char["inventory"].items(),
                   key=lambda kv: kv[1]["qty"] * kv[1]["value"], reverse=True)
    for name, info in items:
        print(f"  {name:10} x{info['qty']}  ({info['qty'] * info['value']} gold)")

pick_up(hero, "sword", 40)
pick_up(hero, "gem", 25, 3)
sell(hero, "potion")
show(hero)
