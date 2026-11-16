import random
import string

def make_password(length=12):
    pools = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
    chars = [random.choice(p) for p in pools]
    everything = "".join(pools)
    chars += [random.choice(everything) for _ in range(length - len(chars))]
    random.shuffle(chars)
    return "".join(chars)

n = int(input("Length (8+): "))
print(make_password(max(n, 8)))
