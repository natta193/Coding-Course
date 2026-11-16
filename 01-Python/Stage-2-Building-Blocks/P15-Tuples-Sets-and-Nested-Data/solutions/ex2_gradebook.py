students = [
    {"name": "Ana", "scores": [78, 85, 92]},
    {"name": "Ben", "scores": [65, 70, 58]},
    {"name": "Cai", "scores": [88, 91, 95]},
    {"name": "Dev", "scores": [55, 61, 72]},
]

def average(nums):
    return sum(nums) / len(nums)

def grade(avg):
    if avg >= 85:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 55:
        return "C"
    return "D"

for s in students:
    a = average(s["scores"])
    print(f"{s['name']:5} {a:5.1f}  {grade(a)}")

all_scores = [x for s in students for x in s["scores"]]
print(f"Class average: {average(all_scores):.1f}")

top = max(students, key=lambda s: average(s["scores"]))
print("Top student:", top["name"])

for s in students:
    sc = s["scores"]
    if all(sc[i] < sc[i + 1] for i in range(len(sc) - 1)):
        print(s["name"], "improved every test")
