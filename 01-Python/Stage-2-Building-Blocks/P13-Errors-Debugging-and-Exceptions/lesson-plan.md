# P13 · Errors, Debugging and Exceptions

**Stage:** Building Blocks  
**Session type:** Lesson (≈60 min)  
**Slides:** `P13-Errors-Debugging-and-Exceptions.pptx`

_Read tracebacks like a pro, use the debugger, and stop programs crashing_

## Learning goals
- Tell syntax, runtime and logic errors apart
- Read a traceback from the bottom up
- Use the VS Code debugger: breakpoints and stepping
- Handle errors with try / except / else / finally

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What is a local variable?  
   **Answer:** A variable created inside a function that only exists while it runs
2. What does `global` do?  
   **Answer:** Lets a function change a global variable
3. What does `if __name__ == "__main__":` do?  
   **Answer:** Runs main() only when the file is run directly, not when it's imported

## Slide outline & tutor notes

**3. Three kinds of error**  
GCSE exam favourite: "identify the type of error on line X". Give quick-fire examples.

**4. Reading a traceback**

**5. Common exceptions**

**6. Debugging strategies**  
Do a live demo of the VS Code debugger on the Collatz program from P05. Watching variables change is a lightbulb moment.

**7. try / except**

**8. Good error handling**

**9. Bug hunt**

**10. Which type of error?**
- `pritn("hello")` → **Runtime – NameError (Python only notices when it reaches that line)**
- `if x > 5` with no colon → **Syntax error**
- `area = width + height` for a rectangle → **Logic error**
- `[1, 2, 3][3]` → **Runtime – IndexError**
- `int("3.5")` → **Runtime – ValueError**

## 🏠 Take-home project: Crash-Proof Tuck Shop
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A tuck-shop till that must NEVER crash, whatever the customer types. Test it by trying to break it!

**Milestones**
1. Store a menu as two lists: item names and prices (in pence, so no float problems)
2. Loop: show the menu, ask for an item number and a quantity – handle letters, negatives and numbers off the menu with try/except and checks
3. Keep a running basket total; "done" finishes the order
4. Ask for the money paid; refuse too little; print the change as coins (£2, £1, 50p, 20p, 10p, 5p, 2p, 1p)
5. Write a test log as comments at the bottom: 8 things you typed to try to break it and what happened

**Stretch:** Add a stock count per item and refuse orders that would take it below 0.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Bug hunt  (★★☆ core)
File: `exercises/ex1_bug_hunt.py`

This program should ask for 5 test scores, then print the average, the highest score and a grade. It has 6 bugs. Fix them all and label each one.

### Crash-proof calculator  (★★☆ core)
File: `exercises/ex2_safe_calculator.py`

Make a calculator that asks for two numbers and an operator (+ - * /). It must never crash: handle letters, division by zero and unknown operators with friendly messages, and loop until the user types "quit".

### Trace table challenge  (★★★ stretch)
File: `exercises/ex3_trace_table.py`

Without running it, fill in a trace table for the mystery function with input 6 (columns: n, i, result). Then run it to check. What does it calculate? Rewrite it with a clearer name.

## Optional extras (if he wants more)
- Make your Higher or Lower game crash-proof: what happens if you type "fish"? Fix it with try/except
- Try the VS Code debugger on your Hangman game and step through one full guess
