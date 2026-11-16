temps = [14, 18, 11, 21, 16]

for t in temps:
    print(f"{t}°C")

print("Total:", sum(temps))
print("Max:", max(temps), "Min:", min(temps))
print("Average:", sum(temps) / len(temps))
print("Sorted:", sorted(temps))

for i, t in enumerate(temps):
    print(f"Day {i + 1}: {t}°C")
