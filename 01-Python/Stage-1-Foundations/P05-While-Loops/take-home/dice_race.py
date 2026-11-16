# TAKE-HOME PROJECT: Dice Race to 50
# After lesson P05 (While Loops) - about 1–2 hours, in chunks over the next few days.
#
# A two-player dice game. Players take turns rolling; first to reach 50 wins. But watch
# out for the special squares!
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Two players take turns. Each turn: press Enter to roll a dice (random.randint(1,
#          6)) and add it to their score
#   [ ] 2. Use a while loop that keeps going until someone reaches 50
#   [ ] 3. Landing exactly on 13 sends you back to 0. Rolling a 6 gives you another roll
#   [ ] 4. Print both scores after every turn
#   [ ] 5. Announce the winner and how many turns the game took
#
# Stretch: Add a computer player that decides whether to "risk it" and roll again or bank
# its score (look up the dice game "Pig" for ideas).
#
# Bring it to the next session - working or stuck, both are fine.

import random

p1 = 0
p2 = 0
