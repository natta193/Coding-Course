import random
import string

# Fake dictionary if you don't have a word list file:
random.seed(1)
WORDS = sorted({"".join(random.choices(string.ascii_lowercase, k=random.randint(2, 7))) for _ in range(5000)}
               | {"the", "cat", "sat", "on", "mat", "a", "dog", "python", "is", "fun"})
