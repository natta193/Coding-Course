class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):          # for print() – friendly
        return f"{self.rank} of {self.suit}"

    def __repr__(self):         # for debugging – precise
        return f"Card({self.rank!r}, {self.suit!r})"

c = Card("Q", "♥")
print(c)          # Q of ♥
print([c])        # [Card('Q', '♥')]
