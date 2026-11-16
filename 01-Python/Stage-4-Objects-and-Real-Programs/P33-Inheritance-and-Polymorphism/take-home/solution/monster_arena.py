import itertools
import random


class Monster:
    def __init__(self, name, hp, attack):
        self.name, self.max_hp, self.hp, self.attack = name, hp, hp, attack

    def reset(self):
        self.hp = self.max_hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, n):
        self.hp = max(0, self.hp - n)

    def act(self, other):
        other.take_damage(self.attack + random.randint(-2, 2))

    def __str__(self):
        return f"{self.name} ({type(self).__name__}) {self.hp}/{self.max_hp}"


class FireDragon(Monster):
    def __init__(self, name):
        super().__init__(name, 60, 9)
        self.burning = 0

    def act(self, other):
        super().act(other)
        if random.random() < 0.3:
            self.burning = 3
        if self.burning:
            other.take_damage(3)
            self.burning -= 1


class Slime(Monster):
    def __init__(self, name):
        super().__init__(name, 70, 6)

    def act(self, other):
        super().act(other)
        self.hp = min(self.max_hp, self.hp + 4)


class Vampire(Monster):
    def __init__(self, name):
        super().__init__(name, 55, 8)

    def act(self, other):
        before = other.hp
        super().act(other)
        self.hp = min(self.max_hp, self.hp + (before - other.hp) // 2)


class Turtle(Monster):
    def __init__(self, name):
        super().__init__(name, 65, 7)
        self.blocking = False

    def take_damage(self, n):
        self.blocking = not self.blocking
        if not self.blocking:
            super().take_damage(n)


def battle(a, b):
    a.reset(); b.reset()
    attacker, defender = random.sample([a, b], 2)
    for _ in range(200):
        attacker.act(defender)
        if not defender.is_alive():
            return attacker
        attacker, defender = defender, attacker
    return a if a.hp >= b.hp else b


monsters = [FireDragon("Ember"), Slime("Gloop"), Vampire("Fang"), Turtle("Shelly")]
wins = {m.name: 0 for m in monsters}
for a, b in itertools.combinations(monsters, 2):
    w = battle(a, b)
    wins[w.name] += 1
    print(f"{a.name} vs {b.name}: {w.name} wins")
print("\nLEAGUE TABLE")
for name, w in sorted(wins.items(), key=lambda kv: -kv[1]):
    print(f"  {name:8} {w} wins")
