class Vehicle:
    def __init__(self, make, model, wheels):
        self.make, self.model, self.wheels = make, model, wheels

    def describe(self):
        return f"{self.make} {self.model} with {self.wheels} wheels"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 4)

class Motorbike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 2)

class Lorry(Vehicle):
    def __init__(self, make, model, cargo_tonnes):
        super().__init__(make, model, 18)
        self.cargo = cargo_tonnes

    def describe(self):
        return super().describe() + f", carries {self.cargo} tonnes"

for v in [Car("Mini", "Cooper"), Motorbike("Honda", "CB500"), Lorry("Volvo", "FH16", 40)]:
    print(v.describe())
