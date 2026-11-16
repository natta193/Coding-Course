import random
secret = random.randint(1, 10)

while True:
    guess = int(input("Guess 1-10: "))
    if guess == secret:
        print("Got it!")
        break
    print("Nope, try again")
