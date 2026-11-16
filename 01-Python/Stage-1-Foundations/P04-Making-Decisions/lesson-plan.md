# P04 · Making Decisions

**Stage:** Foundations  
**Session type:** Lesson (≈60 min)  
**Slides:** `P04-Making-Decisions.pptx`

_if, elif, else – and the Boolean logic underneath_

## Learning goals
- Write if / elif / else blocks with correct indentation
- Use comparison operators == != < > <= >=
- Combine conditions with and, or, not
- Nest decisions and spot when elif is better

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What is `23 % 5`?  
   **Answer:** 3
2. What's the difference between `/` and `//`?  
   **Answer:** / gives a float result; // rounds down to a whole number
3. What does `score += 5` do?  
   **Answer:** Adds 5 to score and stores it back

## Slide outline & tutor notes

**3. if / else**  
Indentation isn't style in Python – it's syntax. Show what happens if you un-indent the second print (it runs regardless).

**4. Comparison operators**

**5. elif: choosing one of many**  
Ask: what if we put `mark >= 50` first? (Everyone above 50 gets a 5.) Order matters!

**6. Boolean logic: and, or, not**  
Explain the bug: "Sun" on its own is a non-empty string, which counts as True ("truthy"). Draw a truth table for AND and OR – it's GCSE content and comes back in P22.

**7. Nested ifs**

**8. Rock, paper, scissors (1 round)**  
There are 9 combinations. Good solutions check draw first, then the 3 ways player 1 wins, else player 2 wins.

**9. True or False?**
- `7 != 7` → **False**
- `3 < 5 and 5 < 4` → **False – the second part is False**
- `not (2 == 3)` → **True**
- `"cat" == "Cat"` → **False – case matters**
- `10 > 5 or 1 / 0` → **True – Python stops early (short-circuits), so the division never runs!**
- `True and not False` → **True**

## 🏠 Take-home project: Choose-Your-Path Story
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Write an interactive story where the reader's choices change what happens. Think "choose your own adventure" book – but in code.

**Milestones**
1. Write an opening scene and ask the player to choose between at least 2 options
2. Each choice leads to a new scene with another choice (at least 2 levels deep, using nested if/elif/else)
3. Have at least 4 different endings – some good, some bad
4. Use `and`/`or` at least once (e.g. "if they have the key AND chose the door")
5. Make typed answers forgiving: `.lower().strip()` so "LEFT " still works

**Stretch:** Track a `health` variable that goes down with bad choices; if it hits 0 the story ends early.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Leap year checker  (★★☆ core)
File: `exercises/ex1_leap_year.py`

A year is a leap year if it's divisible by 4 – except centuries (divisible by 100), which must also be divisible by 400. So 2024 yes, 1900 no, 2000 yes.

### Theme park ride  (★☆☆ warm-up)
File: `exercises/ex2_theme_park.py`

Ask for height (cm) and age. Riders must be at least 140 cm. Under-12s also need an adult (ask y/n). Print whether they can ride and why not if they can't.

### Quadratic solver 2.0  (★★★ stretch)
File: `exercises/ex3_quadratic_v2.py`

Upgrade last lesson's solver: if the discriminant is negative print "No real solutions", if zero print the single solution, otherwise both.

## Optional extras (if he wants more)
- Write a "which superhero are you?" personality quiz with 3 questions and if/elif scoring (invent your own heroes!)
- Draw truth tables for `A and B`, `A or B` and `not A` on paper
