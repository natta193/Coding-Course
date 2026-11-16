# TAKE-HOME PROJECT: Search Showdown
# After lesson P24 (Searching Algorithms) - about 1–2 hours, in chunks over the next few days.
#
# Prove with real data how much faster binary search is – then use it in a game.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Generate a sorted list of 1,000,000 fake usernames (e.g. "user0000001" … with
#          f"user{i:07d}")
#   [ ] 2. Write linear and binary search that also count comparisons
#   [ ] 3. Search for 20 random usernames with both; print a table: name, linear comparisons,
#          binary comparisons
#   [ ] 4. Time both with time.perf_counter() and print the total time for each
#   [ ] 5. Game: the computer thinks of a word from a sorted word list; you guess words and
#          it says "earlier"/"later" in the alphabet – how many guesses do YOU need?
#
# Stretch: Plot comparisons against list size (1,000 → 1,000,000) for both algorithms with
# matplotlib.
#
# Bring it to the next session - working or stuck, both are fine.

import random
import time

users = [f"user{i:07d}" for i in range(1_000_000)]
