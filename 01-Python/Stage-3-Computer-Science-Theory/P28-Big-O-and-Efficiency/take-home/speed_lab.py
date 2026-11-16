# TAKE-HOME PROJECT: Speed Lab Report
# After lesson P28 (Big-O and Efficiency) - about 1–2 hours, in chunks over the next few days.
#
# Be a scientist: measure how three algorithms scale, graph the results and write a
# conclusion.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Pick three functions with different Big-O: e.g. sum of a list (O(n)), bubble sort
#          (O(n²)), binary search (O(log n))
#   [ ] 2. Time each one at n = 1,000, 2,000, 4,000 and 8,000 (repeat each 3 times and take
#          the best)
#   [ ] 3. Print a table of n against time for each function
#   [ ] 4. Plot all three on one graph with matplotlib (log scale on the y-axis helps!)
#   [ ] 5. Write a conclusion in a comment: what happened each time n doubled, and does it
#          match the Big-O?
#
# Stretch: Add x in list vs x in set for the same sizes and explain the result.
#
# Bring it to the next session - working or stuck, both are fine.

import random
import time
import matplotlib.pyplot as plt
