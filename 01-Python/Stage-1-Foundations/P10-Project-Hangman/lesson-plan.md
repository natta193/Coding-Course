# P10 · Project – Hangman

**Stage:** Foundations  
**Session type:** Project session (≈60 min)  
**Slides:** `P10-Project-Hangman.pptx`

_Strings + lists + loops = a real game. End-of-Stage-1 project_

## Learning goals
- Break a bigger problem into steps
- Use lists to track guessed letters and a hidden word
- Use string methods to validate input
- Add ASCII art and polish

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How do you add "kiwi" to the end of a list called fruit?  
   **Answer:** fruit.append("kiwi")
2. What's the difference between `.sort()` and `sorted()`?  
   **Answer:** .sort() changes the list in place; sorted() returns a new sorted list
3. What does `"-".join(["a", "b"])` give?  
   **Answer:** "a-b"

## Slide outline & tutor notes

**3. The brief**

**4. Decompose the problem**  
Computational thinking = decomposition, abstraction, algorithmic thinking. GCSE term – name it.

**5. Milestone 1: show the masked word**

**6. Milestones**

**7. Plan on paper**  
Win check: every letter of secret is in guessed – a loop with a flag, or `all(l in guessed for l in secret)`. Loop condition: lives > 0 and not won.

## 🏠 Take-home project: Hangman Deluxe
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Finish Hangman, then turn it into a deluxe version and do the Stage 1 checkpoint.

**Milestones**
1. Finish milestones M1–M5 from the session
2. Add categories (animals, countries, games…) – the player picks one
3. Add a 2-player mode where one person types the word
4. Do `stage1_checkpoint.py` WITHOUT notes – it tells us what to revise

**Stretch:** Add a hint that reveals one letter but costs 2 lives, and keep score over several rounds.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Hangman – full game  (★★☆ core)
File: `exercises/project_hangman.py`

Build the full game through milestones M1–M5. Test winning, losing, repeated letters and invalid input.

### Stage 1 checkpoint  (★★☆ core)
File: `exercises/stage1_checkpoint.py`

Ten quick questions in checkpoint.py covering everything in Stage 1. Do them without notes – it's for us to see what's stuck and what needs revisiting.

## Optional extras (if he wants more)
- Finish Hangman and add one stretch feature
- Finish the Stage 1 checkpoint if you didn't get through it
