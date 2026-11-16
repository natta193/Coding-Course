# TAKE-HOME PROJECT: Crash-Proof Tuck Shop
# After lesson P13 (Errors, Debugging and Exceptions) - about 1–2 hours, in chunks over the next few days.
#
# A tuck-shop till that must NEVER crash, whatever the customer types. Test it by trying
# to break it!
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Store a menu as two lists: item names and prices (in pence, so no float problems)
#   [ ] 2. Loop: show the menu, ask for an item number and a quantity – handle letters,
#          negatives and numbers off the menu with try/except and checks
#   [ ] 3. Keep a running basket total; "done" finishes the order
#   [ ] 4. Ask for the money paid; refuse too little; print the change as coins (£2, £1, 50p,
#          20p, 10p, 5p, 2p, 1p)
#   [ ] 5. Write a test log as comments at the bottom: 8 things you typed to try to break it
#          and what happened
#
# Stretch: Add a stock count per item and refuse orders that would take it below 0.
#
# Bring it to the next session - working or stuck, both are fine.

ITEMS = ["Crisps", "Chocolate", "Juice", "Apple", "Cookie"]
PRICES = [80, 120, 95, 40, 60]   # pence
