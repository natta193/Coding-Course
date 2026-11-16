import json

ROOMS = {
    "hall": {"desc": "A dusty hall. Stairs lead up.", "exits": {"north": "kitchen", "up": "attic"}, "items": ["torch"]},
    "kitchen": {"desc": "Smells of old cabbage.", "exits": {"south": "hall"}, "items": ["key"]},
    "attic": {"desc": "Pitch black.", "exits": {"down": "hall"}, "items": ["treasure"], "needs": "torch"},
}
SAVE_FILE = "savegame.json"


def describe(state):
    room = ROOMS[state["room"]]
    print(f"\n== {state['room'].upper()} ==")
    print(room["desc"])
    if room["items"]:
        print("You see:", ", ".join(room["items"]))
    print("Exits:", ", ".join(room["exits"]))


def go(state, direction):
    exits = ROOMS[state["room"]]["exits"]
    if direction not in exits:
        print("You can't go that way.")
        return
    target = exits[direction]
    needed = ROOMS[target].get("needs")
    if needed and needed not in state["inventory"]:
        print(f"It's too dangerous without a {needed}.")
        return
    state["room"] = target
    describe(state)


def take(state, item):
    items = ROOMS[state["room"]]["items"]
    if item in items:
        items.remove(item)
        state["inventory"].append(item)
        print(f"Taken: {item}")
    else:
        print(f"There's no {item} here.")


def drop(state, item):
    if item in state["inventory"]:
        state["inventory"].remove(item)
        ROOMS[state["room"]]["items"].append(item)
        print(f"Dropped: {item}")
    else:
        print("You don't have that.")


def save(state):
    with open(SAVE_FILE, "w") as f:
        json.dump({"state": state, "rooms": ROOMS}, f)
    print("Game saved.")


def load():
    with open(SAVE_FILE) as f:
        data = json.load(f)
    ROOMS.clear()
    ROOMS.update(data["rooms"])
    print("Game loaded.")
    return data["state"]


def main():
    state = {"room": "hall", "inventory": []}
    describe(state)
    while True:
        words = input("\n> ").lower().split()
        if not words:
            continue
        verb, noun = words[0], " ".join(words[1:])
        if verb in ["n", "s", "e", "w", "u", "d"]:
            verb, noun = "go", {"n": "north", "s": "south", "e": "east", "w": "west", "u": "up", "d": "down"}[verb]
        if verb == "go":
            go(state, noun)
        elif verb == "take":
            take(state, noun)
        elif verb == "drop":
            drop(state, noun)
        elif verb in ["i", "inventory"]:
            print("You carry:", ", ".join(state["inventory"]) or "nothing")
        elif verb in ["l", "look"]:
            describe(state)
        elif verb == "save":
            save(state)
        elif verb == "load":
            try:
                state = load()
                describe(state)
            except FileNotFoundError:
                print("No saved game.")
        elif verb == "quit":
            break
        else:
            print("I don't understand. Try: go, take, drop, look, inventory, save, load, quit")
        if "treasure" in state["inventory"]:
            print("\n🏆 You found the treasure – you win!")
            break


if __name__ == "__main__":
    main()
