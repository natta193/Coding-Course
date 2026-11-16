import csv
import random

FILE = "cards.csv"

def load():
    try:
        with open(FILE, newline="") as f:
            return [tuple(r) for r in csv.reader(f) if r]
    except FileNotFoundError:
        return []

def save(cards):
    with open(FILE, "w", newline="") as f:
        csv.writer(f).writerows(cards)

def quiz(cards):
    queue = cards[:]
    random.shuffle(queue)
    right = 0
    asked = 0
    while queue:
        q, a = queue.pop(0)
        asked += 1
        if input(q + " ").strip().lower() == a.lower():
            print("✓")
            right += 1
        else:
            print(f"✗ It's {a} – you'll see this one again")
            queue.append((q, a))
    print(f"Done! {right} right out of {asked} attempts")

cards = load()
while True:
    c = input("(a)dd (q)uiz (l)ist e(x)it: ").lower()
    if c == "a":
        cards.append((input("Question: "), input("Answer: ")))
        save(cards)
    elif c == "q" and cards:
        quiz(cards)
    elif c == "l":
        for q, a in cards:
            print(f"{q} → {a}")
    elif c == "x":
        break
