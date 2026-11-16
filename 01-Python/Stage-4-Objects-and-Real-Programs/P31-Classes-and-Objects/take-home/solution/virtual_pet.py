import random


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 3
        self.happiness = 7
        self.energy = 7
        self.age = 0

    @staticmethod
    def clamp(v):
        return max(0, min(10, v))

    def feed(self):
        self.hunger = self.clamp(self.hunger - 4)
        print(f"{self.name} munches happily.")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
            return
        self.happiness = self.clamp(self.happiness + 3)
        self.energy = self.clamp(self.energy - 2)
        self.hunger = self.clamp(self.hunger + 1)
        print(f"{self.name} chases a ball!")

    def sleep(self):
        self.energy = 10
        print(f"{self.name} has a nap. Zzz")

    def tick(self):
        self.age += 1
        self.hunger = self.clamp(self.hunger + random.randint(1, 2))
        self.happiness = self.clamp(self.happiness - 1)
        self.energy = self.clamp(self.energy - 1)

    def is_alive(self):
        return self.hunger < 10 and self.happiness > 0

    def status(self):
        bar = lambda v: "█" * v + "·" * (10 - v)
        print(f"\n{self.name} (age {self.age})")
        print(f"  hunger    {bar(self.hunger)}")
        print(f"  happiness {bar(self.happiness)}")
        print(f"  energy    {bar(self.energy)}")


pet = Pet(input("Name your pet: ") or "Byte")
while pet.is_alive():
    pet.status()
    action = input("(f)eed (p)lay (s)leep (q)uit: ").lower().strip()
    if action == "q":
        break
    elif action == "f":
        pet.feed()
    elif action == "p":
        pet.play()
    elif action == "s":
        pet.sleep()
    pet.tick()
print(f"\n{pet.name} lasted {pet.age} turns." + ("" if pet.is_alive() else " It ran away to find a better owner! 😿"))
