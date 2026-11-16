# C07 · Project – Console Arcade

**Stage:** CSharp Fundamentals  
**Session type:** Project session (≈60 min)  
**Slides:** `C07-Project-Console-Arcade.pptx`

_A menu of mini-games in one C# program – with colour, ReadKey and a high-score file_

## Learning goals
- Structure a bigger C# program with methods
- Use Console features: colours, Clear, ReadKey, SetCursorPosition
- Save and load data with File.ReadAllLines / WriteAllLines
- Port Python ideas to idiomatic C#

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How do you build a long string efficiently?  
   **Answer:** StringBuilder
2. `"hello"[1..4]`?  
   **Answer:** "ell"
3. How do you check if a char is a digit?  
   **Answer:** char.IsDigit(ch)

## Slide outline & tutor notes

**3. The brief**

**4. Console superpowers**

**5. Saving scores to a file**

**6. Milestones**

## 🏠 Take-home project: Arcade Expansion
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Finish your Console Arcade and add a game nobody else has.

**Milestones**
1. Finish milestones M1–M5
2. Invent and add one original mini-game
3. Add a "stats" screen: games played and best score per game
4. Get two people to play; their high scores go in the file

**Stretch:** Port Snake to the console with KeyAvailable and SetCursorPosition.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Console Arcade  (★★☆ core)
File: `exercises/project_console_arcade/Program.cs`

Build the arcade through milestones M1–M5. The reference solution has Higher or Lower, Maths Sprint and a real-time Catch game, plus saved high scores.

## Optional extras (if he wants more)
- Add one more mini-game of your own design
- Get someone at home to play and beat your high scores
