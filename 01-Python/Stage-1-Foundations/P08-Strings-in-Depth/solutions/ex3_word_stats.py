sentence = input("Sentence: ")
words = sentence.split()
print("Words:", len(words))

longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print("Longest word:", longest)

vowels = 0
for ch in sentence.lower():
    if ch in "aeiou":
        vowels += 1
print("Vowels:", vowels)

print("Title case:", sentence.title())

reversed_words = ""
for w in words:
    reversed_words += w[::-1] + " "
print("Reversed words:", reversed_words.strip())
