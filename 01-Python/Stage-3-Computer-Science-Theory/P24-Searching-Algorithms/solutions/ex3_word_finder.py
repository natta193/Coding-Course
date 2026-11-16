import random
import string

random.seed(1)
WORDS = sorted({"".join(random.choices(string.ascii_lowercase, k=random.randint(2, 7))) for _ in range(5000)}
               | {"the", "cat", "sat", "on", "mat", "a", "dog", "python", "is", "fun"})

def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return True
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def spell_check(sentence):
    out = []
    for word in sentence.split():
        clean = word.strip(".,!?").lower()
        out.append(word if binary_search(WORDS, clean) else f"*{word}*")
    return " ".join(out)

print(spell_check("The cat sat on the matt"))
print(spell_check("python is fnu"))
