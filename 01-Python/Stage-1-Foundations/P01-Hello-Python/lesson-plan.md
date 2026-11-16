# P01 · Hello, Python

**Stage:** Foundations  
**Session type:** Lesson (≈60 min)  
**Slides:** `P01-Hello-Python.pptx`

_Set up, write your first programs, and find out what you already know_

## Learning goals
- Install Python + VS Code and run a .py file
- Use print() and comments
- Know what a program, an interpreter and a bug are
- Show what you already know in the diagnostic challenges

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Slide outline & tutor notes

**3. What is a program?**  
Keep this to 2 minutes. Ask him: "What's something you've used today that runs code?" (phone, microwave, car, bus timetable). The big idea is that computers are literal.

**4. Getting set up**  
Do this on his own laptop so he can practise between sessions. Mac: in the VS Code terminal run `bash setup_venv_mac.sh`. Windows: double-click `setup_venv_windows.bat`. Then Cmd/Ctrl+Shift+P → "Python: Select Interpreter" → choose the one in `.venv`.

**5. Virtual environments (venvs)**  
Real developers use a venv for every project. VS Code activates it automatically in new terminals once you've picked it with "Python: Select Interpreter". If `(.venv)` isn't showing, activate it before running pip.

**6. Your first program**  
Get him to type it rather than copy-paste – typing builds muscle memory. Change "Sam" to his name.

**7. Breaking things on purpose**  
Deliberately make errors early so they're not scary. Point out the line number and the little ^ arrow. Line 2 fails because Python is case-sensitive.

**8. Make it yours**  
"Predict, then run" is a habit to build from day one – it forces him to have a mental model.

**9. How Python runs your code**  
The interpreted vs compiled distinction is GCSE content – just plant the seed now; we revisit it properly in C01.

**10. Check your understanding**
- What does `print(3 + 4)` show? → **7**
- What does `print("3 + 4")` show? → **3 + 4 (it's text, so it's printed as-is)**
- Why does `Print("hi")` crash? → **Python is case-sensitive – the function is print, lower case**
- What symbol starts a comment? → **#**

## 🏠 Take-home project: All About Me poster
**Time:** about 1 hour over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Make a program that prints a poster all about you: a big ASCII-art title, a box of facts, a drawing, and a joke with the punchline after a pause. Make it look as good as you can – it's your first real program!

**Milestones**
1. Print a title banner made of characters (search "ASCII text generator" for big letters if you like)
2. Print a box with at least 5 facts about you inside a border of `*` or `#`
3. Draw an ASCII picture of something you like with `print("""...""")`
4. End with a joke: print the setup, then `input("Press Enter...")`, then the punchline
5. Add a comment above every section explaining what it does

**Stretch:** Use `import time` and `time.sleep(0.5)` between lines so the poster appears line by line like a film credit.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Name card  (★☆☆ warm-up)
File: `exercises/ex1_name_card.py`

Print a name card with a border made of stars – at least 5 lines tall.
- Use one print() per line

### ASCII art  (★☆☆ warm-up)
File: `exercises/ex2_ascii_art.py`

Draw a picture using only print() and keyboard characters – a cat, a rocket, a sword. Use triple quotes for multi-line text.

### Diagnostic challenges  (★★☆ core)
File: `exercises/ex3_diagnostic.py`

Five mini-challenges that get harder. Do as many as you can – they help us decide where to start. Don't look anything up!
- Tutor: if he flies through 4 and 5, he can skim P02–P06 quickly.

## Optional extras (if he wants more)
- Install Python + VS Code on your own laptop if not done
- Make a program that prints a joke with the punchline after a blank line
- Find one thing you'd love to build with code (a game? a bot?) – tell me next time
