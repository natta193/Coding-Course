# P05 · While Loops

**Stage:** Foundations  
**Session type:** Lesson (≈60 min)  
**Slides:** `P05-While-Loops.pptx`

_Repeating code until something changes_

## Learning goals
- Write while loops with a condition that eventually becomes False
- Use counters and running totals
- Validate user input with a loop
- Use break and avoid infinite loops

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's wrong with `if x = 5:`?  
   **Answer:** = is assignment; comparison needs ==
2. When does an `else` block run?  
   **Answer:** When none of the if/elif conditions were True
3. What is `True or False and False`?  
   **Answer:** True – and is evaluated before or

## Slide outline & tutor notes

**3. Why loops?**  
Sequence/selection/iteration is the GCSE trio. He now knows all three – that's genuinely enough to write any algorithm.

**4. A counting loop**  
Trace this on paper with a trace table: columns for count, condition, output. Trace tables are a GCSE exam staple.

**5. Input validation**

**6. Running totals and sentinel values**

**7. while True + break**  
Some teachers dislike while True. It's fine when it makes the code clearer – the important thing is there's a guaranteed way out.

**8. Countdown**

**9. How many times does it loop?**
- `i = 0` / `while i < 10:` / `i += 2` → **5 times (0, 2, 4, 6, 8)**
- `i = 10` / `while i > 0:` / `i -= 3` → **4 times (10, 7, 4, 1)**
- `i = 5` / `while i < 5:` / `i += 1` → **0 times – the condition is False from the start**
- `i = 1` / `while i != 10:` / `i += 2` → **Forever! i goes 1, 3, 5, 7, 9, 11… and skips 10**

## 🏠 Take-home project: Dice Race to 50
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A two-player dice game. Players take turns rolling; first to reach 50 wins. But watch out for the special squares!

**Milestones**
1. Two players take turns. Each turn: press Enter to roll a dice (`random.randint(1, 6)`) and add it to their score
2. Use a `while` loop that keeps going until someone reaches 50
3. Landing exactly on 13 sends you back to 0. Rolling a 6 gives you another roll
4. Print both scores after every turn
5. Announce the winner and how many turns the game took

**Stretch:** Add a computer player that decides whether to "risk it" and roll again or bank its score (look up the dice game "Pig" for ideas).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Times table  (★☆☆ warm-up)
File: `exercises/ex1_times_table.py`

Ask for a number and print its times table from 1 to 12 using a while loop, formatted like `7 x 3 = 21`.

### Password checker  (★★☆ core)
File: `exercises/ex2_password.py`

The password is "python123". Give the user 3 attempts. Print "Access granted" or, after 3 wrong goes, "Locked out".

### The Collatz conjecture  (★★★ stretch)
File: `exercises/ex3_collatz.py`

Start with any positive whole number. If it's even, halve it; if it's odd, do 3n + 1. Repeat until you reach 1. Print each step and count how many steps it took. (Mathematicians still can't prove this always reaches 1!)

## Optional extras (if he wants more)
- Write a program that keeps asking for words until the user types "stop", then prints how many words were entered
- Try the Collatz program on 27 and 97. Which number under 100 takes the most steps?
