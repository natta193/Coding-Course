# P12 · Functions II – Scope and Design

**Stage:** Building Blocks  
**Session type:** Lesson (≈60 min)  
**Slides:** `P12-Functions-II-Scope-and-Design.pptx`

_Local vs global variables, default parameters, docstrings and decomposing programs_

## Learning goals
- Explain local and global scope
- Use default parameters and return multiple values
- Write docstrings and type hints
- Structure a program with a main() function

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's the difference between a parameter and an argument?  
   **Answer:** Parameter = variable in the def; argument = value passed in the call
2. What does a function return if it has no return statement?  
   **Answer:** None
3. Why is `return` better than `print` inside a calculation function?  
   **Answer:** The caller can use the returned value in further calculations

## Slide outline & tutor notes

**3. Local scope**

**4. Global scope**  
GCSE asks for advantages of local variables: less memory held, no name clashes, easier to test and reuse. Teach "globals for constants only" as a rule of thumb.

**5. Defaults and multiple returns**

**6. Designing with functions**  
Draw a structure chart (top-down diagram) – GCSE terminology. The __name__ line means the file can be imported without running main.

**7. A well-structured program**

**8. Refactor**  
Refactoring = changing structure without changing behaviour. A professional skill worth naming.

**9. Scope detective**
- `x = 5` / `def f(): x = 10` / `f()` / `print(x)` → **5 – the x inside f is a separate local**
- `def f(a, b=3): return a * b` – what's `f(4)`? → **12**
- `def f(): return 1, 2` – what type does f() return? → **A tuple (1, 2)**
- Can a function call another function? → **Yes – that's how big programs are built**

## 🏠 Take-home project: Refactor the Mess
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Professional programmers spend loads of time cleaning up old code. The starter file is a working but horribly messy times-table quiz. Your job: make it clean WITHOUT changing what it does.

**Milestones**
1. Run it first and play it, so you know exactly what it does
2. Split it into functions: `ask_question()`, `get_number()`, `play_round()`, `show_results()`, `main()`
3. No global variables – pass values in and return them out
4. Give everything a good name and a docstring; delete the copy-pasted code
5. Add `if __name__ == "__main__": main()` – and check it still plays exactly the same

**Stretch:** Add a difficulty setting and a "practise your weakest table" mode – easy now that the code is clean!

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Input helpers module  (★☆☆ warm-up)
File: `exercises/ex1_validators.py`

Write `get_int(prompt)` that keeps asking until a whole number is typed (use `.isdigit()`), `get_yes_no(prompt)` returning True/False, and `get_choice(prompt, options)` that only accepts one of a list of options.

### Stats functions  (★★☆ core)
File: `exercises/ex2_stats.py`

Write `mean(nums)`, `median(nums)`, `mode(nums)` and `range_of(nums)` from scratch (no statistics module). Test them with a few lists including even and odd lengths.

### ATM simulator  (★★★ stretch)
File: `exercises/ex3_atm.py`

Make a cash machine with a balance, PIN check (3 tries), and a menu: balance, deposit, withdraw (can't go below 0), quit. Every feature is its own function; the balance is passed in and returned – no globals.

## Optional extras (if he wants more)
- Draw a structure chart for your Hangman game, then refactor it to match
- Explain to someone at home the difference between local and global variables
