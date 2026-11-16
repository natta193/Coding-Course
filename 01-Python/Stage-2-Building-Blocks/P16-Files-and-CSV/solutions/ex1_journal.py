import datetime

entry = input("How was your day? ")
with open("journal.txt", "a") as f:
    f.write(f"{datetime.date.today()}: {entry}\n")

with open("journal.txt") as f:
    lines = f.readlines()
print("Recent entries:")
for line in lines[-3:]:
    print(" ", line.strip())
