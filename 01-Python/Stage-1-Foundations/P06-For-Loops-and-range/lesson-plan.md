# P06 · For Loops and range()

**Stage:** Foundations  
**Session type:** Lesson (≈60 min)  
**Slides:** `P06-For-Loops-and-range.pptx`

_Count-controlled loops, nested loops and patterns_

## Learning goals
- Use for loops with range(start, stop, step)
- Loop over the characters of a string
- Choose between for and while
- Write nested loops to make grids and patterns

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What are the three parts of a counting while loop?  
   **Answer:** Start value, condition, update
2. What does `break` do?  
   **Answer:** Exits the loop immediately
3. What is a sentinel value?  
   **Answer:** A special input meaning "stop", e.g. 0

## Slide outline & tutor notes

**3. for + range()**  
The "stops before" rule trips everyone up. range(1, 6) means 1 up to but not including 6.

**4. for vs while**

**5. Looping over a string**

**6. Nested loops**

**7. Patterns with loops**

**8. Pyramid builder**

**9. What gets printed?**
- `list(range(3, 8))` → **[3, 4, 5, 6, 7]**
- `list(range(10, 0, -3))` → **[10, 7, 4, 1]**
- How many stars: `for i in range(3):` `for j in range(4): print("*")` → **12**
- `for c in "hi": print(c * 2)` → **hh then ii**
- What's the last value of i in `for i in range(5)`? → **4**

## 🏠 Take-home project: Pattern Studio
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A menu program that draws patterns of any size, using nested for loops. Each pattern is a challenge in working out "how many spaces, how many stars on row r?".

**Milestones**
1. Menu: 1) square 2) right triangle 3) pyramid 4) diamond 5) checkerboard 6) quit – keep showing the menu until they quit
2. Ask for the size and the character to draw with
3. Square and triangle first, then pyramid, then diamond (a pyramid + an upside-down pyramid)
4. Checkerboard: alternate the character and a space – use `(row + col) % 2`
5. Put a blank line after each pattern

**Stretch:** Add a hollow square, a times-table grid with columns lined up, and an "X" shape.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### FizzBuzz  (★☆☆ warm-up)
File: `exercises/ex1_fizzbuzz.py`

Print 1 to 100, but multiples of 3 print "Fizz", multiples of 5 print "Buzz", and multiples of both print "FizzBuzz". (A famous job-interview question!)

### Prime finder  (★★☆ core)
File: `exercises/ex2_primes.py`

Ask for a number n. Print all the prime numbers up to n. A prime has no divisors except 1 and itself. Use a nested loop.

### Chessboard  (★★★ stretch)
File: `exercises/ex3_chessboard.py`

Print an 8×8 chessboard using "██" for black squares and "  " for white. The top-left square is white. Then let the user choose the size.

## Optional extras (if he wants more)
- Print the 12×12 multiplication grid neatly lined up (look up `f"{x:4}"` for padding)
- Write a program that adds up all the numbers from 1 to 1000. Then find the formula that does it without a loop
