# P22 · Logic Gates and Boolean Algebra

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P22-Logic-Gates-and-Boolean-Algebra.pptx`

_From transistors to thinking machines – AND, OR, NOT, XOR and how computers add_

## Learning goals
- Draw truth tables for AND, OR, NOT, XOR, NAND, NOR
- Build logic circuits from Boolean expressions (and back)
- Generate truth tables with Python
- Understand how a half adder and full adder add binary

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What is 1011 in denary?  
   **Answer:** 11
2. How many bits in a nibble?  
   **Answer:** 4
3. What causes an overflow error?  
   **Answer:** A result too big to fit in the number of bits available

## Slide outline & tutor notes

**3. The three basic gates**  
Draw the gate symbols on paper (AND = D shape, OR = curved shield, NOT = triangle with circle). GCSE requires recognising the symbols.

**4. Truth tables with Python**

**5. More gates**  
Fun aside: the "nand2tetris" course builds a full computer from NAND gates up. A great summer project for him in a couple of years.

**6. Expressions → circuits**

**7. How a computer adds: the half adder**  
Draw it. This is the "aha" moment linking P21 and P22 – arithmetic is just logic.

**8. Boolean algebra laws**  
De Morgan is A-level, but he'll use it to simplify if-conditions all the time. Prove it with a truth table program.

**9. Prove De Morgan**

**10. Logic quiz**
- `1 AND 0` → **0**
- `1 XOR 1` → **0**
- `NOT (0 OR 0)` → **1**
- How many rows in a truth table with 4 inputs? → **16**
- In a half adder, which gate gives the carry? → **AND**
- `NAND(1, 1)` → **0**

## 🏠 Take-home project: Circuit Simulator
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Build a little logic-circuit lab: type in any Boolean expression and get its truth table, then use it to solve logic puzzles.

**Milestones**
1. Ask the user for an expression using A, B, C and the words `and`, `or`, `not` (e.g. `(A and B) or not C`)
2. Work out which of A, B, C appear, then print the full truth table (use `itertools.product`)
3. Evaluate safely with `eval(expr, {"__builtins__": {}}, {"A": a, "B": b, "C": c})` – and catch errors from typos
4. Tell the user how many rows are True, and whether the expression is always True (a "tautology")
5. Use it to check both De Morgan's laws and write the results in a comment

**Stretch:** Ask for TWO expressions and report whether they're equivalent (same output on every row).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Truth table generator  (★★☆ core)
File: `exercises/ex1_truth_table.py`

Write `truth_table(func, n)` that prints the full truth table of any Boolean function with n inputs. Use it on several functions including the alarm.

### Everything from NAND  (★★☆ core)
File: `exercises/ex2_gates_from_nand.py`

Write a `nand(a, b)` function. Then write `not_`, `and_`, `or_` and `xor` using ONLY calls to `nand`. Test them against Python's operators for every input.

### Build an 8-bit adder from gates  (★★★ stretch)
File: `exercises/ex3_ripple_adder.py`

Write `half_adder(a, b)` and `full_adder(a, b, carry_in)` using only `&`, `|` and `^`. Chain 8 full adders to add two 8-bit numbers given as lists of bits. Compare with Python's + for 100 random pairs.

## Optional extras (if he wants more)
- Draw the circuit for Q = (A OR B) AND NOT C and its truth table
- Look up "Minecraft redstone adder" – people build these gates in games!
