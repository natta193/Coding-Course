# P40 · Project – Git and the Python Capstone

**Stage:** Objects and Real Programs  
**Session type:** Project session (≈60 min)  
**Slides:** `P40-Project-Git-and-the-Python-Capstone.pptx`

_Version control like a professional, then plan and build your own project (3–5 sessions)_

## Learning goals
- Use Git to track changes: init, add, commit, log, diff
- Push a project to GitHub
- Follow the software development lifecycle to plan a capstone
- Build, test and present a project you designed yourself

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `json.dump` do?  
   **Answer:** Writes a Python object to a file as JSON
2. What does status code 200 mean?  
   **Answer:** OK – the request worked
3. Why handle exceptions around network calls?  
   **Answer:** Networks fail – no connection, timeouts, server errors

## Slide outline & tutor notes

**3. Why version control?**  
Install Git (Mac: `xcode-select --install` or it'll prompt), make a free GitHub account (he's 13 – GitHub's minimum age is 13, so check with parents).

**4. The Git workflow**

**5. The software development lifecycle**  
Real teams use agile – short cycles of this loop. The waterfall vs agile distinction appears at A-level.

**6. Capstone ideas**

**7. Plan your capstone**

## 🏠 Take-home project: Capstone Sprints
**Time:** 2 hours per gap (3–5 gaps) over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Your capstone is your Python graduation project. Work in "sprints": one milestone per gap between sessions.

**Milestones**
1. Make a new folder for it with its OWN venv (`python3 -m venv .venv`) and a requirements.txt
2. Git commit after every work session with a clear message
3. Each gap: one milestone from your plan + update the test plan table
4. Final gap: write the evaluation and prepare a 5-minute demo

**Stretch:** Write a README.md for the repo with screenshots so it works as a portfolio piece.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Git practice  (★☆☆ warm-up)
File: `exercises/git_practice.py`

In a new folder: git init, create hello.py, commit it. Change it, use `git diff` to see the change, commit again. Make a mistake on purpose and use `git restore hello.py` to undo it. View history with `git log --oneline`. Then push the folder to a new GitHub repo.

### Capstone project template  (★★★ stretch)
File: `exercises/capstone_template.py`

A template folder structure for the capstone: README with requirements, a design notes file, main.py with a main() function, a tests file, and a test plan table. Fill it in as you go – this is your Python graduation project!

## Optional extras (if he wants more)
- Commit to your capstone repo after every session – at least 3 commits a week
- Python graduation: present your capstone (5-minute demo + what you'd do next). Then on to C#!
