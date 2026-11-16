# P18 · Project – Quiz Master

**Stage:** Building Blocks  
**Session type:** Project session (≈60 min)  
**Slides:** `P18-Project-Quiz-Master.pptx`

_A multi-category quiz game with questions loaded from a file and a saved leaderboard_

## Learning goals
- Design a program as a set of functions before coding
- Load structured data from a CSV file
- Save and display a persistent leaderboard
- Make the program robust against bad input

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How do you install a package?  
   **Answer:** Activate the venv, then pip install name
2. What does `random.sample(list, 3)` return?  
   **Answer:** 3 different random items from the list
3. How do you import your own helpers.py?  
   **Answer:** import helpers (it must be in the same folder)

## Slide outline & tutor notes

**3. The brief**

**4. Design: the functions**  
This is top-down design from P12. Have him write the def lines with `pass` and docstrings first, then fill them in one at a time, testing each.

**5. The question file**  
One question per row; the header names the columns. csv.DictReader turns each row into a dict. He should write at least 30 questions across 3+ categories (homework).

**6. Milestones**

## 🏠 Take-home project: Quiz Master Content
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Finish Quiz Master and fill it with your own questions.

**Milestones**
1. Finish milestones M3–M5 (rounds, timer bonus, leaderboard)
2. Write at least 30 questions across 3+ categories in questions.csv – include topics you're into
3. Get two people at home to play; save their scores to the leaderboard
4. Fix one thing that confused them

**Stretch:** Add a 50:50 lifeline (removes two wrong answers, once per game).

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Quiz Master – full game  (★★☆ core)
File: `exercises/project_quiz_master.py`

Build Quiz Master through milestones M1–M5. The starter creates a sample questions.csv the first time it runs.

## Optional extras (if he wants more)
- Write at least 30 questions of your own in questions.csv – make some about things you're into
- Get someone at home to play it and watch them: what confused them? Fix it
