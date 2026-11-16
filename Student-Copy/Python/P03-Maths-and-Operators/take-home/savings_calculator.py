# TAKE-HOME PROJECT: Savings Goal Calculator
# After lesson P03 (Maths and Operators) - about 1–2 hours, in chunks over the next few days.
#
# You want to buy something (a game, trainers, a console). Write a calculator that works
# out how long it'll take to save up, using the maths operators from this lesson.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Ask for the item's name and price, how much you've saved already, and your weekly
#          pocket money
#   [ ] 2. Work out how much more you need and how many **whole weeks** it'll take (hint: you
#          can't save for 3.2 weeks – round UP using math.ceil or a trick with //)
#   [ ] 3. Print the date-ish answer in weeks AND as "X months and Y weeks" (assume 4 weeks
#          in a month, use // and %)
#   [ ] 4. If you also do chores for £2 each, how many chores per week would get you there in
#          half the time?
#   [ ] 5. Format all money as £ with 2 decimal places
#
# Stretch: Add 1% interest per week on your savings and use a loop (peek ahead to P05!) to
# see how much sooner you'd get there.
#
# Bring it to the next session - working or stuck, both are fine.

import math

item = input("What do you want to buy? ")
