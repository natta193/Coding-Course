def caesar(text, shift):
    out = ""
    for ch in text:
        if ch.isupper():
            out += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            out += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            out += ch
    return out

while True:
    print("1) reverse 2) encrypt 3) decrypt 4) no vowels 5) pig latin 6) crack 7) quit")
    c = input("> ").strip()
    if c == "7":
        break
    msg = input("Message: ")
    if c == "1":
        print(msg[::-1])
    elif c in ["2", "3"]:
        key = int(input("Key: "))
        print(caesar(msg, key if c == "2" else -key))
    elif c == "4":
        print("".join(ch for ch in msg if ch.lower() not in "aeiou"))
    elif c == "5":
        words = [w[1:] + w[0] + "ay" for w in msg.split() if w]
        print(" ".join(words))
    elif c == "6":
        for s in range(26):
            print(f"{s:2}: {caesar(msg, -s)}")
