print(ord("A"))     # 65
print(ord("a"))     # 97
print(chr(66))      # B
print(chr(128512))  # 😀

# Shift a letter by 3 (Caesar cipher!)
letter = "H"
shifted = chr(ord(letter) + 3)
print(shifted)      # K
