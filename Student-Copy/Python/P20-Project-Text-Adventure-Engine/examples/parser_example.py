def parse(command):
    words = command.lower().split()
    if not words:
        return None, None
    verb = words[0]
    noun = " ".join(words[1:]) or None
    aliases = {"n": ("go", "north"),
               "s": ("go", "south"),
               "i": ("inventory", None)}
    return aliases.get(verb, (verb, noun))

print(parse("take gold key"))
print(parse("n"))  # ('go', 'north')
