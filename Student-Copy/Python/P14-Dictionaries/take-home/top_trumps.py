# TAKE-HOME PROJECT: Top Trumps
# After lesson P14 (Dictionaries) - about 1–2 hours, in chunks over the next few days.
#
# Make a Top Trumps card game against the computer. Each card is a dictionary of stats.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Make at least 10 cards as dictionaries, e.g. {"name": "Dragon", "power": 95,
#          "speed": 60, "magic": 88} (invent your own theme)
#   [ ] 2. Shuffle and deal them into two lists: your hand and the computer's
#   [ ] 3. Each round: show your top card, you choose a stat, compare with the computer's top
#          card
#   [ ] 4. The winner takes both cards (put them at the bottom of their hand). Draws: both
#          cards go back
#   [ ] 5. Play until someone has all the cards (or 20 rounds) – then say who won
#
# Stretch: When the computer wins a round it chooses the stat next time – make it choose
# its best stat.
#
# Bring it to the next session - working or stuck, both are fine.

import random

cards = [
    {"name": "Dragon", "power": 95, "speed": 60, "magic": 88},
]
