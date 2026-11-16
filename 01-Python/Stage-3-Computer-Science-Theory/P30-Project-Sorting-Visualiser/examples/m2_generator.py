def bubble_steps(data):
    n = len(data)
    for p in range(n - 1):
        for i in range(n - 1 - p):
            yield (i, i + 1)                # pause: "I'm comparing these"
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

data = [5, 1, 4, 2]
for pair in bubble_steps(data):
    print(pair, data)
