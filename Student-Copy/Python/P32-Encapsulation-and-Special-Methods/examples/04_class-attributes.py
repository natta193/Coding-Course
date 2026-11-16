class Player:
    count = 0                 # shared by ALL players
    MAX_HP = 100

    def __init__(self, name):
        self.name = name      # each player's own
        self.hp = Player.MAX_HP
        Player.count += 1

a = Player("Ana")
b = Player("Ben")
print(Player.count)    # 2
