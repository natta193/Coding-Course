ITEMS = ["Crisps", "Chocolate", "Juice", "Apple", "Cookie"]
PRICES = [80, 120, 95, 40, 60]   # pence
COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def money(p):
    return f"£{p // 100}.{p % 100:02d}"


def ask_int(prompt, low, high):
    while True:
        text = input(prompt).strip()
        if text.lower() == "done":
            return None
        try:
            n = int(text)
        except ValueError:
            print("  Please type a whole number (or 'done').")
            continue
        if low <= n <= high:
            return n
        print(f"  Must be between {low} and {high}.")


total = 0
while True:
    for i, (name, price) in enumerate(zip(ITEMS, PRICES), 1):
        print(f"{i}) {name:10} {money(price)}")
    item = ask_int("Item number (or 'done'): ", 1, len(ITEMS))
    if item is None:
        break
    qty = ask_int("Quantity: ", 1, 20)
    if qty is None:
        break
    total += PRICES[item - 1] * qty
    print(f"Basket total: {money(total)}\n")

print(f"Total to pay: {money(total)}")
while True:
    try:
        paid = round(float(input("Paid (£): ")) * 100)
    except ValueError:
        print("  Type an amount like 5 or 2.50")
        continue
    if paid >= total:
        break
    print("  That's not enough!")

change = paid - total
print(f"Change: {money(change)}")
for coin in COINS:
    count, change = divmod(change, coin)
    if count:
        print(f"  {count} x {money(coin) if coin >= 100 else str(coin) + 'p'}")

# Test log: "abc" → asked again · "-1" → range error · "99" → range error · "" → asked again
# "done" straight away → £0.00 order · "2.5" quantity → asked again · paid "lots" → asked again · paid too little → refused
