# P17 · Modules and Libraries

**Stage:** Building Blocks  
**Session type:** Lesson (≈60 min)  
**Slides:** `P17-Modules-and-Libraries.pptx`

_Standing on the shoulders of giants – the standard library, your own modules, and pip_

## Learning goals
- Import modules in different ways (import, from…import, as)
- Use random, math, time, datetime and os
- Split your own code into modules
- Install third-party packages with pip

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's the difference between "w" and "a" mode?  
   **Answer:** "w" wipes the file first; "a" adds to the end
2. What does csv.DictReader give you for each row?  
   **Answer:** A dictionary using the header row as keys
3. Why does `f.read() + 1` crash?  
   **Answer:** read() returns a string – you need int() first

## Slide outline & tutor notes

**3. Ways to import**

**4. random: games need chance**  
Ask: how can a computer, which does exactly what it's told, be random? (It can't – pseudo-random from a seed. Real randomness needs physical input.)

**5. time and datetime**

**6. Your own module**

**7. pip: millions of free packages**  
Install pygame now if possible – needed in P35. Also matplotlib for the bonus.

**8. Reaction timer**  
Detecting a false start is genuinely hard in a terminal (input is blocking). Accept "time under 0.1s = false start" as a clever workaround.

**9. Module quiz**
- How do you import only `sqrt` from math? → **from math import sqrt**
- What does `random.seed(1)` do? → **Makes the random numbers repeatable**
- What command installs a package? → **pip install packagename – with the venv activated first**
- Why avoid `from x import *`? → **You can't tell where names came from and they might overwrite yours**

## 🏠 Take-home project: Typing Speed Test
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

How fast can you type? Build a typing test using the random, time and string modules – and save your personal best.

**Milestones**
1. Keep a list of at least 10 sentences; pick one at random with `random.choice`
2. Show it, start a timer when they press Enter, stop it when they finish typing it
3. Work out words per minute (characters ÷ 5 ÷ minutes) and accuracy (% of characters in the right place)
4. Do 3 rounds and print the average WPM
5. Save the best WPM to `best_wpm.txt` (handle the file not existing yet) and say "New record!" when beaten

**Stretch:** Put your helper functions (timing, accuracy) in your own module `typing_tools.py` and import it.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Password generator  (★☆☆ warm-up)
File: `exercises/ex1_password_gen.py`

Generate a random password of a chosen length with at least one upper, one lower, one digit and one symbol. Use the `string` module (`string.ascii_letters`, `string.digits`, `string.punctuation`).

### Birthday facts  (★★☆ core)
File: `exercises/ex2_birthday.py`

Ask for a birth date (YYYY-MM-DD). Print the weekday they were born, their age in days, how many days until their next birthday, and the date they'll be 10,000 days old.

### Estimate π with random darts  (★★★ stretch)
File: `exercises/ex3_monte_carlo.py`

Throw random "darts" at a 1×1 square (x and y between 0 and 1). The fraction that land inside the quarter circle (x² + y² ≤ 1) is about π/4. Estimate π with 1,000, 100,000 and 1,000,000 darts and time each run.

## Optional extras (if he wants more)
- With your venv active, install pygame (`pip install pygame`) and run `python -m pygame.examples.aliens` – we'll make our own game in Stage 4
- Browse the Python docs list of standard library modules and find one that surprises you
