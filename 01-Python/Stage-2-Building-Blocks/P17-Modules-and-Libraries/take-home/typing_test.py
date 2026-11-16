# TAKE-HOME PROJECT: Typing Speed Test
# After lesson P17 (Modules and Libraries) - about 1–2 hours, in chunks over the next few days.
#
# How fast can you type? Build a typing test using the random, time and string modules –
# and save your personal best.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Keep a list of at least 10 sentences; pick one at random with random.choice
#   [ ] 2. Show it, start a timer when they press Enter, stop it when they finish typing it
#   [ ] 3. Work out words per minute (characters ÷ 5 ÷ minutes) and accuracy (% of characters
#          in the right place)
#   [ ] 4. Do 3 rounds and print the average WPM
#   [ ] 5. Save the best WPM to best_wpm.txt (handle the file not existing yet) and say "New
#          record!" when beaten
#
# Stretch: Put your helper functions (timing, accuracy) in your own module typing_tools.py
# and import it.
#
# Bring it to the next session - working or stuck, both are fine.

import random
import time

SENTENCES = [
    "the quick brown fox jumps over the lazy dog",
]
