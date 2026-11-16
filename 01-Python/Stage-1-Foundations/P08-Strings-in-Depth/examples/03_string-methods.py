s = "  Hello, World!  "

print(s.strip())             # "Hello, World!"
print(s.lower())             # "  hello, world!  "
print(s.upper())             # "  HELLO, WORLD!  "
print(s.replace("World", "Sam"))
print(s.count("l"))          # 3
print(s.find("World"))       # 8, or -1
print("hi you".split())      # ['hi', 'you']
print("-".join(["a", "b"]))  # a-b
print("123".isdigit())       # True
