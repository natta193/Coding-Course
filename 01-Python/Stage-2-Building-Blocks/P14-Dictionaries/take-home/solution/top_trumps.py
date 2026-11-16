import random

cards = [
    {"name": "Dragon", "power": 95, "speed": 60, "magic": 88},
    {"name": "Phoenix", "power": 70, "speed": 90, "magic": 92},
    {"name": "Troll", "power": 85, "speed": 20, "magic": 10},
    {"name": "Wizard", "power": 40, "speed": 45, "magic": 99},
    {"name": "Goblin", "power": 30, "speed": 75, "magic": 25},
    {"name": "Griffin", "power": 75, "speed": 85, "magic": 40},
    {"name": "Golem", "power": 90, "speed": 15, "magic": 50},
    {"name": "Sprite", "power": 15, "speed": 95, "magic": 80},
    {"name": "Kraken", "power": 98, "speed": 40, "magic": 60},
    {"name": "Unicorn", "power": 55, "speed": 80, "magic": 85},
]
STATS = ["power", "speed", "magic"]

random.shuffle(cards)
you, cpu = cards[:5], cards[5:]
your_turn = True

for rnd in range(1, 21):
    if not you or not cpu:
        break
    mine, theirs = you.pop(0), cpu.pop(0)
    print(f"\nRound {rnd} – you have {len(you) + 1} cards, computer has {len(cpu) + 1}")
    print(f"Your card: {mine['name']} " + "  ".join(f"{s}={mine[s]}" for s in STATS))
    if your_turn:
        stat = input(f"Choose a stat {STATS}: ").lower().strip()
        while stat not in STATS:
            stat = input("Pick power, speed or magic: ").lower().strip()
    else:
        stat = max(STATS, key=lambda s: theirs[s])
        print(f"Computer chooses {stat}")
    print(f"{mine['name']} {mine[stat]}  vs  {theirs['name']} {theirs[stat]}")
    if mine[stat] > theirs[stat]:
        print("You win the round!")
        you += [mine, theirs]
        your_turn = True
    elif mine[stat] < theirs[stat]:
        print("Computer wins the round.")
        cpu += [theirs, mine]
        your_turn = False
    else:
        print("Draw – cards go back.")
        you.append(mine)
        cpu.append(theirs)

print("\nYOU WIN! 🏆" if len(you) > len(cpu) else "\nThe computer wins." if len(cpu) > len(you) else "\nIt's a tie!")
