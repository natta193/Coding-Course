# TAKE-HOME PROJECT: Leaderboard Sorter
# After lesson P25 (Sorting I – Bubble and Insertion Sort) - about 1–2 hours, in chunks over the next few days.
#
# A game leaderboard sorted by your own sorting algorithms – no `sorted()` or `.sort()`
# allowed!
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Make a list of at least 12 players as tuples: (name, score, time_seconds)
#   [ ] 2. Write insertion_sort(items, key) that sorts by any key function you pass in
#   [ ] 3. Sort by score (highest first); ties broken by time (fastest first) – use a key
#          that returns a tuple like (-score, time)
#   [ ] 4. Print a neat top-10 table with positions, and mark ties
#   [ ] 5. Add new scores typed by the user and keep the board sorted after each one (insert
#          in the right place!)
#
# Stretch: Write bubble sort too, count comparisons for both on 1,000 random players, and
# explain which is better here.
#
# Bring it to the next session - working or stuck, both are fine.

players = [
    ("Ana", 120, 54.2),
    ("Ben", 95, 61.0),
]

def insertion_sort(items, key):
    pass
