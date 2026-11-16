import random

secret = random.randint(1, 100)
guesses = 0
guess = 0

while guess != secret:
    guess = int(input("Your guess: "))
    guesses += 1
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")

print(f"Correct! {guesses} guesses.")
