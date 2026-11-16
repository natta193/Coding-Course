import csv

rows = [["name", "score"], ["Ana", 92], ["Ben", 78]]
with open("scores.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)

with open("scores.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], int(row["score"]))
