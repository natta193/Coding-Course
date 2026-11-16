# TAKE-HOME PROJECT: Circuit Simulator
# After lesson P22 (Logic Gates and Boolean Algebra) - about 1–2 hours, in chunks over the next few days.
#
# Build a little logic-circuit lab: type in any Boolean expression and get its truth
# table, then use it to solve logic puzzles.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Ask the user for an expression using A, B, C and the words and, or, not (e.g. (A
#          and B) or not C)
#   [ ] 2. Work out which of A, B, C appear, then print the full truth table (use
#          itertools.product)
#   [ ] 3. Evaluate safely with eval(expr, {"__builtins__": {}}, {"A": a, "B": b, "C": c}) –
#          and catch errors from typos
#   [ ] 4. Tell the user how many rows are True, and whether the expression is always True (a
#          "tautology")
#   [ ] 5. Use it to check both De Morgan's laws and write the results in a comment
#
# Stretch: Ask for TWO expressions and report whether they're equivalent (same output on
# every row).
#
# Bring it to the next session - working or stuck, both are fine.

from itertools import product

expr = input("Expression using A, B, C: ")
