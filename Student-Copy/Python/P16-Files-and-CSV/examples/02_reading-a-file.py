with open("diary.txt", "r") as f:
    everything = f.read()
print(everything)

with open("diary.txt") as f:      # "r" is default
    for line in f:
        print(line.strip())

with open("diary.txt") as f:
    lines = f.readlines()
print(f"{len(lines)} entries")
