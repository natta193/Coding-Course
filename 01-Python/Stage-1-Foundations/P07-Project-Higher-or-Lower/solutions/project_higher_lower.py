import random

best = None

while True:
    level = input("Difficulty – (e)asy, (m)edium, (h)ard: ").lower()
    while level not in ["e", "m", "h"]:
        level = input("Please type e, m or h: ").lower()
    if level == "e":
        top, lives = 10, 5
    elif level == "m":
        top, lives = 100, 7
    else:
        top, lives = 1000, 10

    secret = random.randint(1, top)
    guesses = 0
    won = False
    print(f"I'm thinking of a number from 1 to {top}. You have {lives} guesses.")

    while guesses < lives:
        guess = int(input("Guess: "))
        guesses += 1
        if guess == secret:
            won = True
            break
        elif guess > secret:
            print("Too high!", end=" ")
        else:
            print("Too low!", end=" ")
        print(f"({lives - guesses} left)")

    if won:
        print(f"🎉 Correct in {guesses} guesses!")
        if best is None or guesses < best:
            best = guesses
            print("New best score!")
    else:
        print(f"Out of guesses – it was {secret}.")

    if best is not None:
        print(f"Best so far: {best}")
    if input("Play again? (y/n) ").lower() != "y":
        print("Thanks for playing!")
        break
