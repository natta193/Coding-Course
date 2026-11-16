import datetime

text = input("Birthday (YYYY-MM-DD): ")
born = datetime.date.fromisoformat(text)
today = datetime.date.today()

print("Born on a", born.strftime("%A"))
print("Age in days:", (today - born).days)

next_bday = born.replace(year=today.year)
if next_bday < today:
    next_bday = next_bday.replace(year=today.year + 1)
print("Days to next birthday:", (next_bday - today).days)
print("10,000 days old on:", born + datetime.timedelta(days=10000))
