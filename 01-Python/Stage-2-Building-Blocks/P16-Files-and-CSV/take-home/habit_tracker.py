# TAKE-HOME PROJECT: Habit Tracker
# After lesson P16 (Files and CSV) - about 1–2 hours, in chunks over the next few days.
#
# A habit tracker that remembers every day you log, using a CSV file. Use it for real for
# a week (reading, practising code, exercise…).
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Each run: ask which habits you did today from a fixed list (y/n for each)
#   [ ] 2. Append a row to habits.csv: date, then 1 or 0 for each habit – write the header
#          row only if the file is new
#   [ ] 3. Don't allow logging the same date twice (read the file first and check)
#   [ ] 4. Report: for each habit, how many days done out of days logged, and the current
#          streak (consecutive days up to today)
#   [ ] 5. Show a mini chart: one █ per day done in the last 7 entries
#
# Stretch: Add a "best streak ever" for each habit and a menu to add a new habit (a new
# column – tricky!).
#
# Bring it to the next session - working or stuck, both are fine.

import csv
import datetime
import os

HABITS = ["read", "code", "exercise"]
FILE = "habits.csv"
