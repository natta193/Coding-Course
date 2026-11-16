import random


def get_number(prompt):
    """Keep asking until the user types a whole number."""
    text = input(prompt)
    while not text.isdigit():
        print("Numbers only.")
        text = input(prompt)
    return int(text)


def ask_question(a, b):
    """Ask a x b. Return True if answered correctly."""
    answer = get_number(f"{a} x {b} = ")
    if answer == a * b:
        print("Correct!")
        return True
    print(f"Wrong – it was {a * b}")
    return False


def play_round(num_questions, low=2, high=12):
    """Play one quiz. Return (score, list of missed questions)."""
    score = 0
    missed = []
    for _ in range(num_questions):
        a, b = random.randint(low, high), random.randint(low, high)
        if ask_question(a, b):
            score += 1
        else:
            missed.append(f"{a} x {b}")
    return score, missed


def show_results(score, total, missed):
    """Print the score, a comment and anything to practise."""
    print(f"You got {score} out of {total}")
    if score == total:
        print("Perfect!")
    elif score > total / 2:
        print("Good work.")
    else:
        print("Keep practising.")
    if missed:
        print("Practise these:", ", ".join(missed))


def main():
    total = get_number("How many questions? ")
    score, missed = play_round(total)
    show_results(score, total, missed)


if __name__ == "__main__":
    main()
