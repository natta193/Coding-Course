# P03 · Maths and Operators

**Stage:** Foundations  
**Session type:** Lesson (≈60 min)  
**Slides:** `P03-Maths-and-Operators.pptx`

_Python as a super-calculator – and the operators every programmer uses daily_

## Learning goals
- Use + - * / // % ** and know the difference between / and //
- Apply operator precedence (BIDMAS) and brackets
- Use the shorthand += -= *=
- Use `round()`, `abs()`, `min()`, `max()` and the math module

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What type does `input()` always return?  
   **Answer:** str (a string)
2. How do you turn "12" into the number 12?  
   **Answer:** int("12")
3. What does `f"{3.14159:.2f}"` give?  
   **Answer:** 3.14

## Slide outline & tutor notes

**3. The arithmetic operators**  
GCSE uses DIV and MOD for // and %. Make sure he can say "17 MOD 5 = 2" fluently.

**4. Why % (modulo) is secretly amazing**  
Ask him: what's 135 seconds in minutes and seconds? Then show the // and % solution.

**5. Order of operations**

**6. Shortcuts and handy functions**  
Python has no ++ operator (unlike C#). We'll see `count++` again in C#.

**7. Floats aren't perfect**  
This links to binary in Stage 3. Great "whoa" moment – lean into it.

**8. Rounding surprises**  
Ask: 61 people, 15 per minibus – how many minibuses? (math.ceil(61/15) = 5). Comes up in the P03 take-home.

**9. Time converter**  
Hint if stuck: days = s // 86400, then s = s % 86400, and repeat for hours (3600) and minutes (60).

**10. Predict the output**
- `17 // 5` → **3**
- `17 % 5` → **2**
- `2 ** 3 ** 2` → **512 – powers go right to left: 3**2 = 9, then 2**9**
- `10 / 4` → **2.5**
- `(4 + 6) * 2 - 3` → **17**
- `x = 5` then `x *= 3` – what's x? → **15**

## 🏠 Take-home project: Savings Goal Calculator
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

You want to buy something (a game, trainers, a console). Write a calculator that works out how long it'll take to save up, using the maths operators from this lesson.

**Milestones**
1. Ask for the item's name and price, how much you've saved already, and your weekly pocket money
2. Work out how much more you need and how many **whole weeks** it'll take (hint: you can't save for 3.2 weeks – round UP using `math.ceil` or a trick with `//`)
3. Print the date-ish answer in weeks AND as "X months and Y weeks" (assume 4 weeks in a month, use // and %)
4. If you also do chores for £2 each, how many chores per week would get you there in half the time?
5. Format all money as £ with 2 decimal places

**Stretch:** Add 1% interest per week on your savings and use a loop (peek ahead to P05!) to see how much sooner you'd get there.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Circle calculator  (★☆☆ warm-up)
File: `exercises/ex1_circle.py`

Ask for a radius. Print the circle's area (πr²) and circumference (2πr), rounded to 2 dp. Use `math.pi`.

### Digit splitter  (★★☆ core)
File: `exercises/ex2_digits.py`

Ask for a 3-digit number. Using only // and %, print the hundreds, tens and units digits and their sum. (No converting to a string!)

### Quadratic solver  (★★★ stretch)
File: `exercises/ex3_quadratic.py`

Ask for a, b and c in ax² + bx + c = 0. Use the quadratic formula to print both solutions. (Don't worry about negative discriminants yet – that needs `if`, next lesson.)

## Optional extras (if he wants more)
- Write a program that converts a height in cm to feet and inches (1 inch = 2.54 cm, 12 inches = 1 foot) using // and %
- Find out what `divmod(17, 5)` does and explain it next session
