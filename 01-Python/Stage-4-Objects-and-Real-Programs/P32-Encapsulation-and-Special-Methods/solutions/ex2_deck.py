import random

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♠", "♥", "♦", "♣"]

class Card:
    def __init__(self, rank, suit):
        self.rank, self.suit = rank, suit

    @property
    def value(self):
        return RANKS.index(self.rank) + 2

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f"{self.rank}{self.suit}"

    __repr__ = __str__

class Deck:
    def __init__(self):
        self.cards = [Card(r, s) for s in SUITS for r in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        hand, self.cards = self.cards[:n], self.cards[n:]
        return hand

    def __len__(self):
        return len(self.cards)

deck = Deck()
deck.shuffle()
p1, p2 = deck.deal(5), deck.deal(5)
print("Player 1:", sorted(p1), "high:", max(p1))
print("Player 2:", sorted(p2), "high:", max(p2))
print(len(deck), "cards left")
