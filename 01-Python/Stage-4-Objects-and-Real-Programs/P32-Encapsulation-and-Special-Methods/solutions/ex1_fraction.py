import math

class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError("denominator can't be 0")
        if den < 0:
            num, den = -num, -den
        g = math.gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __add__(self, o):
        return Fraction(self.num * o.den + o.num * self.den, self.den * o.den)

    def __sub__(self, o):
        return Fraction(self.num * o.den - o.num * self.den, self.den * o.den)

    def __mul__(self, o):
        return Fraction(self.num * o.num, self.den * o.den)

    def __eq__(self, o):
        return self.num == o.num and self.den == o.den

    def __lt__(self, o):
        return self.num * o.den < o.num * self.den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

print(Fraction(1, 2) + Fraction(1, 3))            # 5/6
print(Fraction(2, 4) == Fraction(1, 2))           # True
print(sorted([Fraction(3, 4), Fraction(1, 3), Fraction(1, 2)]))
