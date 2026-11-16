import random

players = [
    ("Ana", 120, 54.2), ("Ben", 95, 61.0), ("Cai", 120, 49.8), ("Dev", 80, 70.1),
    ("Eli", 140, 66.3), ("Fay", 95, 58.9), ("Gus", 60, 45.0), ("Hal", 140, 62.0),
    ("Ivy", 110, 50.5), ("Jon", 75, 80.2), ("Kim", 130, 59.9), ("Lou", 100, 57.7),
]


def insertion_sort(items, key):
    items = items[:]
    for i in range(1, len(items)):
        cur = items[i]
        j = i - 1
        while j >= 0 and key(items[j]) > key(cur):
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = cur
    return items


def rank_key(p):
    return (-p[1], p[2])


def show(board):
    print(f"{'#':>2}  {'Name':6} {'Score':>5} {'Time':>6}")
    for i, (name, score, t) in enumerate(board[:10]):
        tie = " (tie)" if i > 0 and board[i - 1][1] == score else ""
        print(f"{i + 1:>2}. {name:6} {score:>5} {t:>6.1f}{tie}")


board = insertion_sort(players, rank_key)
show(board)
while True:
    name = input("\nNew player name (blank to stop): ").strip()
    if not name:
        break
    score = int(input("Score: "))
    t = float(input("Time (s): "))
    new = (name, score, t)
    pos = 0
    while pos < len(board) and rank_key(board[pos]) <= rank_key(new):
        pos += 1
    board.insert(pos, new)
    show(board)
