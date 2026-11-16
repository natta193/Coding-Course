import csv
import os
import random
import time

SAMPLE = """category,question,a,b,c,d,answer
Science,What is H2O?,Salt,Water,Gold,Air,b
Science,What planet is closest to the Sun?,Venus,Earth,Mercury,Mars,c
Computing,What does CPU stand for?,Central Processing Unit,Computer Power Unit,Core Program Utility,Central Program Unit,a
Computing,How many bits in a byte?,4,8,16,32,b
Geography,Capital of Australia?,Sydney,Melbourne,Canberra,Perth,c
Geography,Longest river in the world?,Amazon,Thames,Nile,Yangtze,c
"""
QUESTIONS_FILE = "questions.csv"
BOARD_FILE = "leaderboard.csv"
ROUND_LENGTH = 10


def load_questions(filename):
    """Return a list of question dictionaries."""
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(SAMPLE)
    with open(filename, newline="") as f:
        return list(csv.DictReader(f))


def choose_category(questions):
    cats = sorted({q["category"] for q in questions})
    for i, c in enumerate(cats, 1):
        print(f"{i}) {c}")
    print(f"{len(cats) + 1}) Mixed")
    while True:
        choice = input("Category: ")
        if choice.isdigit() and 1 <= int(choice) <= len(cats) + 1:
            n = int(choice)
            return None if n == len(cats) + 1 else cats[n - 1]
        print("Pick a number from the list.")


def ask_question(q):
    """Ask one question; return the points scored."""
    print("\n" + q["question"])
    for letter in "abcd":
        print(f"  {letter.upper()}) {q[letter]}")
    start = time.time()
    ans = input("Answer: ").strip().lower()
    while ans not in ["a", "b", "c", "d"]:
        ans = input("Type A, B, C or D: ").strip().lower()
    taken = time.time() - start
    if ans == q["answer"]:
        points = 20 if taken < 5 else 10
        print(f"Correct! +{points} ({taken:.1f}s)")
        return points
    print(f"Wrong – it was {q['answer'].upper()}) {q[q['answer']]}")
    return 0


def play(questions, category):
    pool = [q for q in questions if category is None or q["category"] == category]
    chosen = random.sample(pool, min(ROUND_LENGTH, len(pool)))
    return sum(ask_question(q) for q in chosen)


def save_score(name, score):
    with open(BOARD_FILE, "a", newline="") as f:
        csv.writer(f).writerow([name, score])


def show_leaderboard():
    try:
        with open(BOARD_FILE, newline="") as f:
            rows = [(n, int(s)) for n, s in csv.reader(f)]
    except FileNotFoundError:
        rows = []
    rows.sort(key=lambda r: r[1], reverse=True)
    print("\n🏆 LEADERBOARD")
    for i, (n, s) in enumerate(rows[:10], 1):
        print(f"{i:2}. {n:12} {s}")


def main():
    questions = load_questions(QUESTIONS_FILE)
    name = input("Your name: ").strip() or "Anonymous"
    category = choose_category(questions)
    score = play(questions, category)
    print(f"\nWell done {name}, you scored {score}!")
    save_score(name, score)
    show_leaderboard()


if __name__ == "__main__":
    main()
