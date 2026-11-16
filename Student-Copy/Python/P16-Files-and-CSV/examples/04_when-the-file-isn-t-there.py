def load_high_score():
    try:
        with open("highscore.txt") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

best = load_high_score()
print("Best so far:", best)
