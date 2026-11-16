import random

class Fighter:
    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        damage = max(1, amount - self.defence)
        self.hp = max(0, self.hp - damage)
        return damage

    def attack_target(self, other):
        power = self.attack + random.randint(-2, 2)
        crit = random.random() < 0.1
        if crit:
            power *= 2
        dealt = other.take_damage(power)
        msg = " CRITICAL HIT!" if crit else ""
        print(f"{self.name} hits {other.name} for {dealt}.{msg} ({other.name}: {other.hp} HP)")

knight = Fighter("Knight", 40, 9, 3)
goblin = Fighter("Goblin", 30, 7, 1)
attacker, defender = knight, goblin
while knight.is_alive() and goblin.is_alive():
    attacker.attack_target(defender)
    attacker, defender = defender, attacker
winner = knight if knight.is_alive() else goblin
print(f"🏆 {winner.name} wins!")
