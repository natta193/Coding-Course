import random

scores = [0, 0]
player = 0
turns = 0

while max(scores) < 50:
    turns += 1
    input(f"Player {player + 1}, press Enter to roll...")
    roll = random.randint(1, 6)
    scores[player] += roll
    print(f"  Rolled a {roll} → {scores[player]}")
    while roll == 6 and scores[player] < 50:
        print("  A six! Roll again.")
        roll = random.randint(1, 6)
        scores[player] += roll
        print(f"  Rolled a {roll} → {scores[player]}")
    if scores[player] == 13:
        print("  Unlucky 13! Back to 0.")
        scores[player] = 0
    print(f"Scores: P1 {scores[0]}  |  P2 {scores[1]}\n")
    if scores[player] >= 50:
        break
    player = 1 - player

print(f"🏆 Player {player + 1} wins after {turns} turns!")
