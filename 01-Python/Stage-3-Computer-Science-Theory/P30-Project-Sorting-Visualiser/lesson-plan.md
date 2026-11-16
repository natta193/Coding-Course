# P30 · Project – Sorting Visualiser

**Stage:** Computer Science Theory  
**Session type:** Project session (≈60 min)  
**Slides:** `P30-Project-Sorting-Visualiser.pptx`

_Watch bubble, insertion, merge and quicksort race – drawn live with turtle_

## Learning goals
- Animate an algorithm step by step
- Use generators (yield) to pause an algorithm mid-way
- Connect theory (Big-O) to something you can see
- Ship a polished, configurable program

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Stack: LIFO or FIFO?  
   **Answer:** LIFO – last in, first out
2. What's the best Python structure for a queue?  
   **Answer:** collections.deque
3. How do you check brackets are balanced?  
   **Answer:** Push openers onto a stack; each closer must match the popped top; stack must be empty at the end

## Slide outline & tutor notes

**3. The brief**

**4. Drawing bars**

**5. The trick: yield**  
Generators are an intermediate Python feature, but this is the perfect use case. Explain: "yield = return, but it remembers where it was".

**6. Milestones**

## 🏠 Take-home project: Visualiser Upgrades
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Finish the sorting visualiser and add features, then do the Stage 3 checkpoint.

**Milestones**
1. Finish milestones M1–M5
2. Add starting-data options: random, nearly sorted, reversed – which sort wins each?
3. Record a screen video of your favourite sort to show next session
4. Do the Stage 3 checkpoint without notes

**Stretch:** Race two algorithms side by side in one window.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Sorting visualiser – full program  (★★☆ core)
File: `exercises/project_sort_visualiser.py`

Build the visualiser through milestones M1–M5. The solution supports bubble, insertion, merge and quick sort with highlighting and counters.

### Stage 3 checkpoint  (★★☆ core)
File: `exercises/stage3_checkpoint.py`

Theory + code questions on Stage 3. Answer the theory ones in comments.

## Optional extras (if he wants more)
- Add one stretch feature to the visualiser and record a screen video of it to show off
- Finish the Stage 3 checkpoint
