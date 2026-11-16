import random

class Animal:
    food = "food"
    noise = "..."

    def __init__(self, name):
        self.name = name
        self.hunger = 3

    def new_day(self):
        self.hunger = min(10, self.hunger + random.randint(1, 3))

    def feed(self):
        self.hunger = max(0, self.hunger - 5)

    def special(self):
        return ""

    def __str__(self):
        return f"{type(self).__name__} {self.name} (hunger {self.hunger})"

class Lion(Animal):
    food, noise = "meat", "ROAR"
    def special(self):
        return f"{self.name} sleeps for 20 hours."

class Penguin(Animal):
    food, noise = "fish", "honk"
    def special(self):
        return f"{self.name} slides on its belly!"

class Monkey(Animal):
    food, noise = "bananas", "ooh-ooh"
    def special(self):
        return f"{self.name} steals a visitor's hat."

class Parrot(Animal):
    food, noise = "seeds", "Hello!"
    def special(self):
        return f"{self.name} says '{random.choice(['Pieces of eight', 'Feed me', 'Python!'])}'"

class Enclosure:
    def __init__(self, name):
        self.name = name
        self.animals = []

class Zoo:
    def __init__(self):
        self.enclosures = []

    def all_animals(self):
        return [a for e in self.enclosures for a in e.animals]

    def run_day(self, day):
        print(f"\n--- Day {day} ---")
        for a in self.all_animals():
            a.new_day()
            if random.random() < 0.3:
                print(a.special())
            if a.hunger > 6:
                print(f"{a.name} goes '{a.noise}' and eats {a.food}.")
                a.feed()
        hungry = [a for a in self.all_animals() if a.hunger > 4]
        print("Still peckish:", ", ".join(a.name for a in hungry) or "nobody")

zoo = Zoo()
big_cats, water, trees = Enclosure("Big cats"), Enclosure("Pool"), Enclosure("Jungle")
big_cats.animals += [Lion("Leo"), Lion("Nala")]
water.animals += [Penguin("Pingu"), Penguin("Waddles")]
trees.animals += [Monkey("George"), Parrot("Polly")]
zoo.enclosures += [big_cats, water, trees]
for day in range(1, 8):
    zoo.run_day(day)
