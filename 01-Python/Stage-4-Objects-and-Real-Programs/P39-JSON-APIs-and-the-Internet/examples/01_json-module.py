import json

player = {"name": "Ana", "level": 7,
          "items": ["sword", "potion"], "alive": True}

text = json.dumps(player)            # dict -> JSON string
print(text)
back = json.loads(text)              # JSON string -> dict

with open("save.json", "w") as f:
    json.dump(player, f, indent=2)   # straight to a file
with open("save.json") as f:
    loaded = json.load(f)
print(loaded["items"][0])            # sword
