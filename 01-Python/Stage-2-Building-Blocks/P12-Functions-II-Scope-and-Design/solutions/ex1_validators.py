def get_int(prompt):
    text = input(prompt)
    while not text.lstrip("-").isdigit():
        print("Please enter a whole number.")
        text = input(prompt)
    return int(text)

def get_yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n) ").lower().strip()
        if ans in ["y", "yes"]:
            return True
        if ans in ["n", "no"]:
            return False

def get_choice(prompt, options):
    ans = input(f"{prompt} {options}: ")
    while ans not in options:
        ans = input(f"Choose one of {options}: ")
    return ans

if __name__ == "__main__":
    age = get_int("Age: ")
    pizza = get_yes_no("Like pizza?")
    colour = get_choice("Colour", ["red", "green", "blue"])
    print(age, pizza, colour)
