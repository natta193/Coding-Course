class Dog:
    def __init__(self, name, breed):
        self.name = name          # attributes
        self.breed = breed
        self.energy = 10

    def bark(self):               # method
        print(f"{self.name} says Woof!")

    def play(self, minutes):
        self.energy -= minutes // 10
        print(f"{self.name} has {self.energy} energy left")

rex = Dog("Rex", "Labrador")     # create an object
bella = Dog("Bella", "Poodle")
rex.bark()
bella.play(30)
