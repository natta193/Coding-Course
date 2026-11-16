import random


def to_binary(n, width=8):
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits.rjust(width, "0")


def to_denary(bits):
    total = 0
    for b in bits:
        total = total * 2 + int(b)
    return total


level = input("Level – (e)asy or (h)ard? ").lower()
top, width = (15, 4) if level.startswith("e") else (255, 8)
score = streak = 0
wrong = []

for q in range(1, 11):
    n = random.randint(0, top)
    kind = random.choice(["to_bin", "to_den", "to_hex"])
    if kind == "to_bin":
        question, answer = f"{n} in binary ({width} bits)", to_binary(n, width)
    elif kind == "to_den":
        question, answer = f"{to_binary(n, width)} in denary", str(n)
    else:
        question, answer = f"{n} in hex", format(n, "X")
    reply = input(f"Q{q}: {question}? ").strip().upper()
    if reply == answer.upper() or (kind == "to_bin" and reply.rjust(width, "0") == answer):
        score += 1
        streak += 1
        if streak % 3 == 0:
            score += 1
            print("✓ Streak bonus!")
        else:
            print("✓")
    else:
        streak = 0
        wrong.append((question, answer))
        print(f"✗ It was {answer}")

print(f"\nScore: {score}")
for qn, ans in wrong:
    print(f"  {qn} = {ans}")
