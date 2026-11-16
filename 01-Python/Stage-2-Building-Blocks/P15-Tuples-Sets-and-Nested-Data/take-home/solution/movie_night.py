import random

movies = [
    {"title": "Space Rescue", "year": 2021, "rating": 12, "minutes": 118, "genres": ["sci-fi", "action"]},
    {"title": "The Haunted Pier", "year": 2019, "rating": 15, "minutes": 104, "genres": ["horror"]},
    {"title": "Robot Puppy", "year": 2023, "rating": 0, "minutes": 92, "genres": ["comedy", "sci-fi", "family"]},
    {"title": "Goal!", "year": 2018, "rating": 12, "minutes": 110, "genres": ["sport", "drama"]},
    {"title": "Dragon School", "year": 2022, "rating": 8, "minutes": 99, "genres": ["fantasy", "comedy", "family"]},
    {"title": "Heist Club", "year": 2020, "rating": 12, "minutes": 125, "genres": ["action", "comedy"]},
    {"title": "Deep Ocean", "year": 2017, "rating": 0, "minutes": 85, "genres": ["documentary"]},
    {"title": "Mars Base", "year": 2024, "rating": 12, "minutes": 131, "genres": ["sci-fi", "drama"]},
]

n = int(input("How many friends? "))
shared = None
youngest = 200
for i in range(n):
    age = int(input(f"Friend {i + 1} age: "))
    likes = {g.strip().lower() for g in input("Genres they like (comma-separated): ").split(",")}
    youngest = min(youngest, age)
    shared = likes if shared is None else shared & likes

print("Everyone likes:", shared or "nothing in common!")
shortlist = [m for m in movies if m["rating"] <= youngest and shared & set(m["genres"])]
shortlist.sort(key=lambda m: m["minutes"])
for m in shortlist:
    print(f"  {m['title']} ({m['year']}) – {m['minutes']} min")

if shortlist:
    votes = {}
    for i in range(n):
        choice = input(f"Friend {i + 1}, vote for a title: ").strip()
        if any(m["title"] == choice for m in shortlist):
            votes[choice] = votes.get(choice, 0) + 1
    if votes:
        top = max(votes.values())
        print("Tonight's film:", random.choice([t for t, v in votes.items() if v == top]))
    else:
        print("Tonight's film:", random.choice(shortlist)["title"])
else:
    print("No films everyone can watch – board games instead?")
