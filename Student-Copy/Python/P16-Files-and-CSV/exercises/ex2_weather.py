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

# now read weather.csv with csv.DictReader and analyse it
