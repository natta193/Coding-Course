class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def intro(self):
        return f"I'm {self.name} and I say {self.speak()}"

class Dog(Animal):
    def speak(self):            # override
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

print(Dog("Rex").intro())   # I'm Rex and I say Woof
print(Cat("Tom").intro())   # I'm Tom and I say Meow
