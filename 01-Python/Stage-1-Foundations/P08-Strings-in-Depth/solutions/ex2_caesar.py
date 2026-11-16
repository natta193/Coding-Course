message = input("Message: ")
shift = int(input("Shift: "))
result = ""

for ch in message:
    if ch.isupper():
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch

print("Encrypted:", result)
