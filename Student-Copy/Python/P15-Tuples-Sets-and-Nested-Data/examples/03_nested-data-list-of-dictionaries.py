students = [
    {"name": "Ana", "age": 13, "scores": [78, 85, 92]},
    {"name": "Ben", "age": 14, "scores": [65, 70, 58]},
    {"name": "Cai", "age": 13, "scores": [88, 91, 95]},
]

for s in students:
    avg = sum(s["scores"]) / len(s["scores"])
    print(f"{s['name']}: {avg:.1f}")

print(students[2]["scores"][0])   # 88
students.append({"name": "Dev", "age": 13, "scores": []})
