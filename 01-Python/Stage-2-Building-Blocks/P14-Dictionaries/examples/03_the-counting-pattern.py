text = "the cat and the hat and the bat"
counts = {}

for word in text.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
# shorter: counts[word] = counts.get(word, 0) + 1
