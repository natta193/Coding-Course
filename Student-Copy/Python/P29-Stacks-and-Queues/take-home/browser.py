# TAKE-HOME PROJECT: Browser History
# After lesson P29 (Stacks and Queues) - about 1–2 hours, in chunks over the next few days.
#
# Simulate a web browser's Back and Forward buttons with two stacks, plus a "recently
# visited" list with a queue.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Commands: visit <url>, back, forward, history, quit
#   [ ] 2. Visiting pushes the current page onto the back stack and clears the forward stack
#   [ ] 3. Back pops from the back stack and pushes the current page onto the forward stack
#          (and Forward does the reverse)
#   [ ] 4. Keep the last 5 visited pages in a deque(maxlen=5) and show them with history
#   [ ] 5. Handle Back/Forward when the stack is empty with a friendly message
#
# Stretch: Add bookmark and bookmarks commands using a set (no duplicates).
#
# Bring it to the next session - working or stuck, both are fine.

from collections import deque

back_stack = []
forward_stack = []
current = "home"
