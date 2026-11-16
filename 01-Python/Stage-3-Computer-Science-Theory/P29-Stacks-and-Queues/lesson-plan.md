# P29 · Stacks and Queues

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P29-Stacks-and-Queues.pptx`

_Two simple data structures that run undo buttons, browsers, printers and games_

## Learning goals
- Explain LIFO (stack) and FIFO (queue) with real examples
- Implement push, pop, peek, enqueue, dequeue, is_empty
- Use a stack to check brackets and evaluate expressions
- Use collections.deque for efficient queues

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's the Big-O of looking something up in a set?  
   **Answer:** O(1) on average
2. What's the Big-O of a loop inside a loop over the same data?  
   **Answer:** O(n²)
3. Simplify O(3n² + 5n + 7)  
   **Answer:** O(n²)

## Slide outline & tutor notes

**3. Abstract data types**

**4. LIFO vs FIFO**

**5. A stack with a list**

**6. A queue with deque**  
A-level also covers circular queues and priority queues – the stretch exercise does a circular one.

**7. Stacks solve brackets**

**8. Undo button**

**9. Stack or queue?**
- Undo in a word processor → **Stack**
- People waiting for a rollercoaster → **Queue**
- Push A, push B, pop, push C, pop, pop – what order were things removed? → **B, C, A**
- Enqueue 1, 2, 3, dequeue, enqueue 4, dequeue – what's left? → **[3, 4]**
- Why is `list.pop(0)` slow for big queues? → **Every remaining item shifts one place left – O(n)**

## 🏠 Take-home project: Browser History
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Simulate a web browser's Back and Forward buttons with two stacks, plus a "recently visited" list with a queue.

**Milestones**
1. Commands: `visit <url>`, `back`, `forward`, `history`, `quit`
2. Visiting pushes the current page onto the back stack and clears the forward stack
3. Back pops from the back stack and pushes the current page onto the forward stack (and Forward does the reverse)
4. Keep the last 5 visited pages in a `deque(maxlen=5)` and show them with `history`
5. Handle Back/Forward when the stack is empty with a friendly message

**Stretch:** Add `bookmark` and `bookmarks` commands using a set (no duplicates).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Build your own Stack and Queue  (★★☆ core)
File: `exercises/ex1_stack_class.py`

Write Stack and Queue as sets of functions acting on a list (we'll turn them into classes in P31). Include is_empty, size, and error messages when popping from an empty structure.

### Reverse Polish calculator  (★★☆ core)
File: `exercises/ex2_rpn.py`

In Reverse Polish Notation the operator comes after its operands: `3 4 + 2 *` means (3 + 4) × 2. Evaluate RPN with a stack: numbers are pushed; an operator pops two, applies itself, pushes the result.

### Circular queue  (★★★ stretch)
File: `exercises/ex3_circular_queue.py`

Implement a fixed-size circular queue using a list of size n plus front/rear pointers and a count – no shifting! When rear reaches the end it wraps to index 0 (hello, modulo). Simulate a printer queue with it.

## Optional extras (if he wants more)
- Write out what happens to the call stack when `factorial(4)` runs (P26) – it's a stack!
- Find two more real-life examples of stacks and two of queues
