ROOMS = {
    "hall": {
        "desc": "A dusty hall. Stairs lead up.",
        "exits": {"north": "kitchen", "up": "attic"},
        "items": ["torch"],
    },
    "kitchen": {
        "desc": "Smells of old cabbage.",
        "exits": {"south": "hall"},
        "items": ["key"],
    },
    "attic": {
        "desc": "Pitch black.",
        "exits": {"down": "hall"},
        "items": ["treasure"],
        "needs": "torch",
    },
}
