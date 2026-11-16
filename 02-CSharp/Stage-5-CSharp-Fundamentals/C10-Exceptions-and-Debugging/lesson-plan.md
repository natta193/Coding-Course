# C10 · Exceptions and Debugging

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C10-Exceptions-and-Debugging.pptx`

_try/catch/finally, throwing your own exceptions, and the VS Code debugger for C#_

## Learning goals
- Catch exceptions with try / catch / finally
- Throw exceptions and create custom exception classes
- Prefer TryParse-style validation where it fits
- Debug C# with breakpoints, watches and the call stack

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `: base(name)` do?  
   **Answer:** Calls the parent class constructor
2. Abstract class vs interface?  
   **Answer:** Abstract class: an "is a" base with shared code, single inheritance. Interface: a "can do" contract, many allowed
3. What keyword lets a child replace a parent method?  
   **Answer:** override (the parent must be virtual/abstract)

## Slide outline & tutor notes

**3. try / catch / finally**

**4. Common .NET exceptions**

**5. Throwing and custom exceptions**

**6. Filters and rethrowing**

**7. Exceptions vs Try-pattern**

**8. Debugging C# in VS Code**  
Do a live debugging session on his C09 RPG code: put a breakpoint in TakeDamage and watch Health change. Conditional breakpoints are a superpower for loops.

**9. Make it crash-proof**

**10. Exceptions quiz**
- Which exception does `int.Parse("hi")` throw? → **FormatException**
- Order catch blocks from…? → **Most specific to most general (Exception last)**
- When does `finally` run? → **Always – whether or not an exception happened**
- Exceptions or TryParse for user input? → **TryParse – bad input is expected, not exceptional**
- What's `nameof(amount)`? → **The string "amount" – the compiler checks the name exists**

## 🏠 Take-home project: Bulletproof Bank
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Upgrade your bank account into a program that handles every error properly and keeps a log file.

**Milestones**
1. Custom exceptions: `InsufficientFundsException` (with the shortfall) and `AccountLockedException`
2. PIN entry: 3 wrong tries locks the account (throw AccountLockedException; catch it in the menu)
3. Every transaction is appended to `transactions.log` with the date and time
4. Withdrawals and deposits validate amounts and throw `ArgumentOutOfRangeException` for ≤ 0
5. The menu catches each exception type separately with a friendly message – the program never crashes

**Stretch:** Read `transactions.log` back at start-up to rebuild the balance (and skip corrupt lines).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Crash-proof calculator  (★☆☆ warm-up)
File: `exercises/ex1_safe_calculator/Program.cs`

Port P13's calculator: parse two numbers and an operator; handle FormatException, DivideByZeroException (use `decimal` – double gives Infinity instead!) and unknown operators (throw InvalidOperationException). Loop until "quit".

### Bug hunt  (★★☆ core)
File: `exercises/ex2_bug_hunt/Program.cs`

This program should read 5 scores, store them, and print the average, the top score and the grade. It has compile errors, runtime exceptions and logic errors. Use the compiler and the debugger to fix them all and comment each fix.

### Robust high-score file  (★★★ stretch)
File: `exercises/ex3_safe_file/Program.cs`

Write a `HighScores` class that loads "name,score" lines from a file. Corrupt lines (missing comma, non-number score) must be skipped and counted, not crash. A missing file means an empty table. Saving must not lose data if writing fails half-way (write to a temp file, then `File.Move` with overwrite).

## Optional extras (if he wants more)
- Find a NullReferenceException in one of your programs (or cause one!) and fix it using the debugger
- Look up C#'s `?.` (null-conditional) and `??=` operators – we'll use them in C12
