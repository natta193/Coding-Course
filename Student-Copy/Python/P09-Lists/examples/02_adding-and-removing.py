pets = ["cat", "dog"]
pets.append("fish")       # add to end
pets.insert(0, "rabbit")  # add at position 0
print(pets)  # ['rabbit', 'cat', 'dog', 'fish']

last = pets.pop()         # remove & return last
pets.remove("cat")        # remove by value
del pets[0]               # remove by index
print(pets, last)         # ['dog'] fish

print("dog" in pets)      # True
