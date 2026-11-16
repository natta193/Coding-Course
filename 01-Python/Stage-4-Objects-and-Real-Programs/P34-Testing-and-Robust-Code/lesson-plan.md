# P34 · Testing and Robust Code

**Stage:** Objects and Real Programs  
**Session type:** Lesson (≈60 min)  
**Slides:** `P34-Testing-and-Robust-Code.pptx`

_Proving your code works – test plans, assert, pytest and defensive programming_

## Learning goals
- Write a test plan with normal, boundary, invalid and erroneous data
- Use assert to check assumptions
- Write and run unit tests with pytest
- Apply defensive design: validation, sanitisation, authentication

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `class Dog(Animal):` mean?  
   **Answer:** Dog is a subclass of Animal and inherits its attributes and methods
2. What is polymorphism?  
   **Answer:** Different classes responding to the same method call in their own way
3. When should you use composition over inheritance?  
   **Answer:** When it's a "has a" relationship rather than "is a"

## Slide outline & tutor notes

**3. Why test?**  
Ariane 5 (1996): a 64-bit float converted to a 16-bit int overflowed – rocket self-destructed 37s after launch. Links back to overflow in P21!

**4. Test data types (GCSE)**  
Off-by-one errors (< vs <=) are the most common bug in the world. Boundary testing catches them.

**5. assert**

**6. Unit tests with pytest**

**7. Many tests at once: parametrize**

**8. Defensive design**  
SQL injection is the famous example of what happens without sanitisation – xkcd "Bobby Tables" is worth showing.

**9. Test plan**

**10. Testing quiz**
- An age field accepts 13–19. Give two boundary values → **13 and 19 (and 12/20 just outside)**
- What type of test data is "twelve" for an age? → **Erroneous**
- What's the difference between iterative and final testing? → **Iterative = testing each part during development; final = testing the whole finished program**
- What does pytest look for? → **Files and functions whose names start with test_**
- Name 3 kinds of validation check → **Any of: type, range, length, presence, format**

## 🏠 Take-home project: Bug Bounty
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

The starter is a little "text utilities" module with 5 hidden bugs. Your job: write tests that FIND them, then fix the code. Real testers do exactly this.

**Milestones**
1. Read each function's docstring – that's the spec of what it SHOULD do
2. Write at least 2 pytest tests per function in `test_bug_bounty.py` (normal + boundary + erroneous data)
3. Run `pytest -v` (venv active!) – every failing test is a bug found
4. Fix the bugs one at a time until everything passes
5. Write a short bug report in a comment: what was wrong in each function

**Stretch:** Add a new function `is_valid_email(s)` – write the tests FIRST (TDD), then the code.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Test-driven: password validator  (★★☆ core)
File: `exercises/ex1_tdd.py`

Test-driven development: write the tests FIRST. The rules: 8–20 chars, at least one digit, one upper, one lower, no spaces. Write 8+ pytest tests, watch them fail, then write `is_valid_password` until they all pass.

### Test your sorts  (★★☆ core)
File: `exercises/ex2_test_sorts.py`

Write pytest tests for your merge sort and binary search from Stage 3: empty list, one item, duplicates, already sorted, reversed, negative numbers, and 100 random lists compared with sorted().

### Robust sign-up form  (★★★ stretch)
File: `exercises/ex3_robust_form.py`

Build a sign-up form that validates: username (3–15 chars, letters/digits/underscore only, not already taken), email (format check), age (13–120), password (your validator). Re-ask each field until valid with a specific error message. Store users in a JSON file with the password **hashed** (hashlib.sha256) – never store plain passwords!

## Optional extras (if he wants more)
- Install pytest and run the tests from ex1 and ex2 with `pytest -v`
- Find one bug in an old program of yours with a boundary test
