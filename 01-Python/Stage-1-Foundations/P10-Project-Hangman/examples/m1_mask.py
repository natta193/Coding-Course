secret = "python"
guessed = ["p", "o"]

display = ""
for letter in secret:
    if letter in guessed:
        display += letter + " "
    else:
        display += "_ "
print(display)
