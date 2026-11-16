students.sort(key=lambda s: s["age"])

best = max(students, key=lambda s: sum(s["scores"]))
print(best["name"])

names = [s["name"] for s in students if s["age"] == 13]
print(names)    # list comprehension
