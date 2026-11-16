# TAKE-HOME PROJECT: Big Sort
# After lesson P27 (Sorting II – Merge Sort and Quicksort) - about 1–2 hours, in chunks over the next few days.
#
# Sort a really big file with your own merge sort and compare it with Python's built-in
# sort.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Write a program that creates words.txt with 200,000 random "words" (random
#          letters, 3–8 long), one per line
#   [ ] 2. Read it back into a list and sort it with YOUR merge sort; check the result equals
#          sorted()
#   [ ] 3. Time your merge sort, your quicksort and sorted() on it and print a results table
#   [ ] 4. Find the 10 most common words (sorting makes duplicates sit next to each other –
#          use that, no dictionary!)
#   [ ] 5. Write the sorted words to sorted_words.txt
#
# Stretch: Find out what algorithm Python's sorted() uses (Timsort) and why it's faster
# than yours, in 3 sentences in a comment.
#
# Bring it to the next session - working or stuck, both are fine.

import random
import string
import time
