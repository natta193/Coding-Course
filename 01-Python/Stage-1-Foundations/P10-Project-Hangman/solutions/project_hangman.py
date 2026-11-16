import random

WORDS = ["python", "variable", "function", "keyboard", "galaxy", "puzzle"]
STAGES = [
    "",
    "  O",
    "  O\n  |",
    "  O\n /|",
    "  O\n /|\\",
    "  O\n /|\\\n /",
    "  O\n /|\\\n / \\",
]

secret = random.choice(WORDS)
guessed = []
lives = 6

while lives > 0:
    display = ""
    won = True
    for letter in secret:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
            won = False
    print("\n" + STAGES[6 - lives])
    print(display)
    if won:
        print("You win! 🎉")
        break

    guess = input(f"Guess a letter ({lives} lives): ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please type a single letter.")
        continue
    if guess in guessed:
        print(f"You already tried {guess}.")
        continue

    guessed.append(guess)
    if guess not in secret:
        lives -= 1
        print(f"No {guess} in the word!")
else:
    print(STAGES[6])
    print(f"Game over – the word was {secret}.")
