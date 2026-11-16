# P16 · Files and CSV

**Stage:** Building Blocks  
**Session type:** Lesson (≈60 min)  
**Slides:** `P16-Files-and-CSV.pptx`

_Making data survive after the program closes_

## Learning goals
- Read and write text files with open() and with
- Know the modes r, w and a
- Read and write CSV files with the csv module
- Handle missing files gracefully

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Give one difference between a tuple and a list  
   **Answer:** Tuples are immutable (can't be changed); lists can
2. What does `{1, 2} & {2, 3}` give?  
   **Answer:** {2} – the intersection
3. How do you get Cai's first score from `students[2]["scores"][0]`?  
   **Answer:** Item 2 of the list, its "scores" key, item 0 of that list

## Slide outline & tutor notes

**3. Why files?**  
Volatile/non-volatile and primary/secondary storage are GCSE hardware topics – worth the 30-second tangent.

**4. Writing a file**

**5. Reading a file**

**6. CSV: tables in text files**

**7. When the file isn't there**

**8. High score saver**

**9. Files quiz**
- Which mode wipes the file first? → **"w"**
- What type is everything you read from a text file? → **str**
- Why use `with`? → **It closes the file automatically, even if an error happens**
- What exception happens opening a file that doesn't exist for reading? → **FileNotFoundError**
- How do you add to a file without deleting its contents? → **Open it in "a" (append) mode**

## 🏠 Take-home project: Habit Tracker
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A habit tracker that remembers every day you log, using a CSV file. Use it for real for a week (reading, practising code, exercise…).

**Milestones**
1. Each run: ask which habits you did today from a fixed list (y/n for each)
2. Append a row to `habits.csv`: date, then 1 or 0 for each habit – write the header row only if the file is new
3. Don't allow logging the same date twice (read the file first and check)
4. Report: for each habit, how many days done out of days logged, and the current streak (consecutive days up to today)
5. Show a mini chart: one █ per day done in the last 7 entries

**Stretch:** Add a "best streak ever" for each habit and a menu to add a new habit (a new column – tricky!).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Journal app  (★☆☆ warm-up)
File: `exercises/ex1_journal.py`

Each run, ask "How was your day?" and append the answer to journal.txt with the date (`import datetime; datetime.date.today()`). Then print the last 3 entries.

### Weather data analysis  (★★☆ core)
File: `exercises/ex2_weather.py`

weather.csv (create it with the starter) has date, max temp, min temp and rainfall. Print the hottest day, the total rainfall, the average max temp and the number of dry days.

### Flashcard revision app  (★★★ stretch)
File: `exercises/ex3_flashcards.py`

Store flashcards (question,answer) in cards.csv. Menu: add a card, quiz me (random order, score shown at end), list cards. Cards the user gets wrong should be asked again at the end of the round.

## Optional extras (if he wants more)
- Use your flashcard app to revise something for school this week
- Download a CSV from the internet (e.g. Premier League table, Pokémon stats) and write 3 questions your program answers about it
