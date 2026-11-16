# P23 · Algorithms, Pseudocode and Flowcharts

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P23-Algorithms-Pseudocode-and-Flowcharts.pptx`

_Thinking like a computer scientist before writing a line of code_

## Learning goals
- Use the computational thinking skills: decomposition, abstraction, algorithmic thinking
- Read and write exam-style pseudocode
- Draw and follow flowcharts with the standard symbols
- Complete trace tables to dry-run algorithms

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does XOR output when both inputs are 1?  
   **Answer:** 0
2. Which two gates make a half adder?  
   **Answer:** XOR (sum) and AND (carry)
3. State one of De Morgan's laws  
   **Answer:** NOT(A AND B) = NOT A OR NOT B (or the OR version)

## Slide outline & tutor notes

**3. What is an algorithm?**

**4. Computational thinking**  
Ask him for a non-computing example of abstraction (a football formation diagram, a recipe, a game's minimap).

**5. Pseudocode (exam style)**  
AQA, OCR and Edexcel all use slightly different pseudocode. Check which board his school uses and get a copy of that board's reference sheet.

**6. Flowchart symbols**  
Draw the flowchart for the pseudocode on the previous slide together. Loops are a decision with one arrow pointing back.

**7. Trace tables: be the computer**

**8. Trace this**

**9. Write, draw, trace**

**10. Algorithm quiz**
- Which computational thinking skill is a tube map an example of? → **Abstraction**
- What flowchart shape is used for a decision? → **Diamond**
- In pseudocode, what does `x ← x + 1` mean? → **Add 1 to x and store it back in x**
- Three properties of a good algorithm? → **Unambiguous, finite, correct**
- What's the point of a trace table? → **To dry-run an algorithm and track variable values, finding logic errors**

## 🏠 Take-home project: Check-Digit Detective
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Real-world algorithm time. ISBNs (on every book) and bank cards have a "check digit" that catches typing mistakes. Design the algorithms properly before coding them.

**Milestones**
1. For ISBN-13: write pseudocode first – multiply digits alternately by 1 and 3, add them up; valid if the total is divisible by 10
2. Code `valid_isbn13(code)` (ignore dashes) and test it on 3 books from your shelf
3. Look up the Luhn algorithm (used by bank cards) and write it as pseudocode AND a flowchart on paper
4. Code `valid_luhn(number)` and test it on `4539 1488 0343 6467` (valid) and `4539 1488 0343 6468` (invalid)
5. Fill in a trace table for one of them in a comment at the bottom

**Stretch:** Write `make_isbn13(first12)` that calculates the missing 13th digit.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Pseudocode → Python  (★☆☆ warm-up)
File: `exercises/ex1_pseudocode_to_python.py`

Translate the three pseudocode algorithms in the starter into Python and run them.

### Trace table puzzles  (★★☆ core)
File: `exercises/ex2_trace_puzzles.py`

For each mystery function: trace it on paper for the given input, predict the output, then run it. Write a one-line comment saying what each algorithm does in general.

### Design an algorithm: change machine  (★★★ stretch)
File: `exercises/ex3_design_algorithm.py`

A vending machine must give change using the fewest coins (UK coins: 200, 100, 50, 20, 10, 5, 2, 1 pence). Write the pseudocode FIRST, then the Python. Does the greedy approach always give the fewest coins? Try a made-up coin system [1, 3, 4] with 6p.

## Optional extras (if he wants more)
- Get a copy of your exam board's pseudocode guide (ask your CS teacher which board) and read it
- Draw a flowchart for your morning routine with at least two decisions
