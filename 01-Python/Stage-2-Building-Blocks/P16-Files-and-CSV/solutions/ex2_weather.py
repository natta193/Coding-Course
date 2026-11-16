import csv

DATA = """date,max_temp,min_temp,rain_mm
2026-06-01,19,11,0
2026-06-02,22,13,2.5
2026-06-03,25,14,0
2026-06-04,17,10,8.1
2026-06-05,21,12,0
2026-06-06,27,16,0
2026-06-07,18,11,4.0
"""
with open("weather.csv", "w") as f:
    f.write(DATA)

with open("weather.csv") as f:
    days = list(csv.DictReader(f))

hottest = max(days, key=lambda d: float(d["max_temp"]))
total_rain = sum(float(d["rain_mm"]) for d in days)
avg_max = sum(float(d["max_temp"]) for d in days) / len(days)
dry = len([d for d in days if float(d["rain_mm"]) == 0])

print(f"Hottest: {hottest['date']} ({hottest['max_temp']}°C)")
print(f"Total rain: {total_rain:.1f} mm")
print(f"Average max: {avg_max:.1f}°C")
print(f"Dry days: {dry}")
