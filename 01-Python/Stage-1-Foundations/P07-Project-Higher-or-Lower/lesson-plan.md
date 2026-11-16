# P07 · Project – Higher or Lower

**Stage:** Foundations  
**Session type:** Project session (≈60 min)  
**Slides:** `P07-Project-Higher-or-Lower.pptx`

_Build a complete number-guessing game with difficulty levels and a high score_

## Learning goals
- Plan a program before coding it
- Combine input, if/elif, loops and random in one program
- Build in small milestones, testing after each one
- Add polish: replay, difficulty, scoring

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Which loop would you use for "keep asking until correct"?  
   **Answer:** while
2. What does `range(2, 11, 2)` give?  
   **Answer:** 2, 4, 6, 8, 10
3. How do you get a random number from 1 to 100?  
   **Answer:** import random, then random.randint(1, 100)

## Slide outline & tutor notes

**3. The brief**  
Before touching the keyboard, get him to describe the game in steps on paper (pseudocode). 5 minutes of planning saves 20 of debugging.

**4. Plan first: pseudocode**  
GCSE pseudocode style. No exact syntax needed – it's about the logic.

**5. Milestone 1: the core loop**

**6. Milestones 2–5**  
Reverse mode is a brilliant intro to binary search (P24) – the computer should always guess the middle of the remaining range. Plant the seed: "what's the best strategy?"

**7. Before you build**  
Answer: 7, because 2^7 = 128 ≥ 100. Halving each time. Don't explain yet – come back to it in P24.

## 🏠 Take-home project: Finish Higher or Lower
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Finish the milestones you didn't get to in the session, then make the game your own.

**Milestones**
1. Finish milestones 2–5 (difficulty, lives, play again, best score)
2. Add the reverse mode where the computer guesses YOUR number
3. Make the computer as smart as possible – how many guesses does it need at most for 1–100? Why?
4. Ask someone at home to play and watch them – fix anything that confuses them

**Stretch:** Add a two-player mode: player 1 types a secret number (hide it by printing 50 blank lines), player 2 guesses.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Higher or Lower – full game  (★★☆ core)
File: `exercises/project_higher_lower.py`

Build the full game through milestones 1–5. Test after each milestone. The solution file shows one complete version – yours can look different!
- Milestones are on the slide before.

### Reverse mode: computer guesses  (★★★ stretch)
File: `exercises/reverse_mode.py`

You think of a number 1–100. The computer guesses; you reply h (too high), l (too low) or c (correct). Make the computer as smart as possible.

## Optional extras (if he wants more)
- Finish any milestones you didn't get to
- Add one feature of your own (sound with `print("\a")`, ASCII-art title screen, a timer using `time.time()`…)
