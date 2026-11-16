import csv
import datetime
import os

HABITS = ["read", "code", "exercise"]
FILE = "habits.csv"


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, newline="") as f:
        return list(csv.DictReader(f))


def log_today(rows):
    today = str(datetime.date.today())
    if any(r["date"] == today for r in rows):
        print("Already logged today!")
        return rows
    row = {"date": today}
    for h in HABITS:
        row[h] = "1" if input(f"Did you {h} today? (y/n) ").lower().startswith("y") else "0"
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date"] + HABITS)
        if new_file:
            w.writeheader()
        w.writerow(row)
    return rows + [row]


def streak(rows, habit):
    count = 0
    for r in reversed(rows):
        if r[habit] == "1":
            count += 1
        else:
            break
    return count


rows = log_today(load())
print(f"\n{len(rows)} days logged")
for h in HABITS:
    done = sum(int(r[h]) for r in rows)
    chart = "".join("█" if r[h] == "1" else "·" for r in rows[-7:])
    print(f"{h:9} {done}/{len(rows)}  streak {streak(rows, h)}  last 7: {chart}")
