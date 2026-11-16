class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Wizard(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)   # parent sets name, hp
        self.mana = mana             # then add our own

    def cast(self):
        if self.mana >= 10:
            self.mana -= 10
            return 25
        return 0

w = Wizard("Merlin", 60, 30)
print(w.name, w.hp, w.mana)
