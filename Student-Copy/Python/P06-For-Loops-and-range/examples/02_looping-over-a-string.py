word = "python"
for letter in word:
    print(letter.upper())

vowels = 0
for ch in "programming is fun":
    if ch in "aeiou":
        vowels += 1
print(f"{vowels} vowels")
