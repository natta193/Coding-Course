mark = int(input("Mark out of 100: "))

if mark >= 90:
    grade = "9"
elif mark >= 80:
    grade = "8"
elif mark >= 70:
    grade = "7"
elif mark >= 50:
    grade = "5"
else:
    grade = "U"

print(f"Grade: {grade}")
