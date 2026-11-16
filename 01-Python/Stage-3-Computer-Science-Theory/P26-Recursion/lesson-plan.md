# P26 · Recursion

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P26-Recursion.pptx`

_Functions that call themselves – the most elegant idea in programming_

## Learning goals
- Explain recursion: base case + recursive case
- Trace recursive calls using the call stack
- Write recursive versions of factorial, sum, power and binary search
- Know the risks: stack overflow and repeated work

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does one pass of bubble sort guarantee?  
   **Answer:** The largest unsorted item reaches its final position at the end
2. How does insertion sort work?  
   **Answer:** Takes each item and slides it left into place in the sorted part
3. Both have worst case about how many comparisons for n items?  
   **Answer:** About n² (n²/2)

## Slide outline & tutor notes

**3. What is recursion?**  
You've already seen it – the fractal tree in P19. Russian dolls are the classic analogy.

**4. Factorial**

**5. The call stack**  
Draw the stack as a pile of plates. Show it live in the VS Code debugger – the CALL STACK panel shows each frame.

**6. More recursive classics**

**7. Recursive binary search**

**8. Recursion vs iteration**

**9. Recursive warm-ups**

**10. Recursion quiz**
- What two things does every recursive function need? → **A base case and a recursive case moving towards it**
- What happens with no base case? → **Infinite recursion → RecursionError (stack overflow)**
- `def f(n): return 0 if n == 0 else n + f(n - 1)` – what's f(4)? → **10**
- What data structure does Python use to track function calls? → **The call stack**

## 🏠 Take-home project: Recursion Puzzle Pack
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Five puzzles that are hard with loops and beautiful with recursion. Each needs a base case and a recursive case – write them as comments first.

**Milestones**
1. `sierpinski(n)` – return a list of strings drawing the Sierpinski triangle in text (n=0 is just `*`)
2. `permutations(word)` – every ordering of the letters (check "abc" gives 6)
3. `flood_fill(grid, r, c, new)` – "paint bucket": fill the connected area of same characters in a 2D list
4. `count_paths(rows, cols)` – how many ways to walk from the top-left to bottom-right of a grid, only moving right or down
5. `power_set(items)` – every subset of a list (there should be 2ⁿ)

**Stretch:** `count_paths(16, 16)` is very slow – fix it with memoisation (a dictionary) like fib in the lesson.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Fibonacci – the slow way and the fast way  (★★☆ core)
File: `exercises/ex1_fibonacci.py`

Fibonacci: fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2). Write it recursively and time fib(30). Count how many calls it makes. Then fix it by remembering answers in a dictionary (memoisation) and compare.

### Recursive toolkit  (★★☆ core)
File: `exercises/ex2_recursive_toolkit.py`

Write recursively (only flatten may use a loop): `digit_sum(n)`, `count(items, x)`, `flatten(nested)` which turns `[1, [2, [3, 4]], 5]` into `[1, 2, 3, 4, 5]`, and `binary(n)` which returns n as a binary string.

### Towers of Hanoi  (★★★ stretch)
File: `exercises/ex3_hanoi.py`

Move n discs from peg A to peg C using peg B, never putting a bigger disc on a smaller one. The recursive insight: move n-1 discs out of the way, move the biggest, move the n-1 back on top. Print every move and count them. How many moves for 64 discs?

## Optional extras (if he wants more)
- Write a recursive function that prints all permutations (orderings) of a word, e.g. "abc" → abc, acb, bac, bca, cab, cba
- Revisit the fractal tree from P19 – can you now explain exactly how it works?
