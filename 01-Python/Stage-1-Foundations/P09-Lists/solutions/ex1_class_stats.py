marks = []
n = int(input("How many students? "))
for i in range(n):
    marks.append(int(input(f"Mark for student {i + 1}: ")))

avg = sum(marks) / len(marks)
above = 0
for m in marks:
    if m > avg:
        above += 1

print(f"Highest {max(marks)}, lowest {min(marks)}, average {avg:.1f}")
print(f"{above} students above average")
