import random
import time

SENTENCES = [
    "the quick brown fox jumps over the lazy dog",
    "python is a great first programming language",
    "practice makes progress not perfection",
    "a bug in the code is worth two in the docs",
    "computers do exactly what you tell them",
    "every expert was once a beginner",
    "loops let you repeat things without copying",
    "functions are like recipes you can reuse",
    "debugging is twice as hard as writing code",
    "the best way to learn is to build things",
]
BEST_FILE = "best_wpm.txt"


def accuracy(target, typed):
    correct = sum(1 for a, b in zip(target, typed) if a == b)
    return 100 * correct / max(len(target), 1)


def load_best():
    try:
        with open(BEST_FILE) as f:
            return float(f.read())
    except (FileNotFoundError, ValueError):
        return 0.0


results = []
for rnd in range(1, 4):
    sentence = random.choice(SENTENCES)
    print(f"\nRound {rnd}:\n  {sentence}")
    input("Press Enter, then type it as fast as you can...")
    start = time.time()
    typed = input("> ")
    minutes = (time.time() - start) / 60
    wpm = len(typed) / 5 / max(minutes, 1e-6)
    acc = accuracy(sentence, typed)
    print(f"{wpm:.0f} WPM, {acc:.0f}% accurate")
    results.append(wpm)

avg = sum(results) / len(results)
print(f"\nAverage: {avg:.0f} WPM")
best = load_best()
if avg > best:
    print("🏆 New record!")
    with open(BEST_FILE, "w") as f:
        f.write(str(avg))
else:
    print(f"Personal best is {best:.0f} WPM")
