# Python Tutor Guide (Stages 1–4, P01–P40)

## Overview
- 40 lessons, 1 h each, ~every 3 days, + a 1–2 h take-home after each. Most coding happens at home.
- Stage 1 Foundations → 2 Building Blocks → 3 CS Theory (GCSE + some A-level) → 4 OOP, Pygame, testing, APIs, Git, capstone.
- ⭐ = project lesson (P07, P10, P18, P20, P30, P37, P40); P37/P40 run 2–5 sessions.
- ~22–25 weeks at the planned pace. Then C# (see `CSharp-Guide.md`).
- All solutions (in-session + take-home) have been run; Pygame ones smoke-tested headless.

```
<stage>/<lesson>/
  <lesson>.pptx      slides – answers + tutor notes in speaker notes
  lesson-plan.md     timings, recap/quiz answers, tutor notes, exercise briefs
  examples/          every code snippet on the slides
  exercises/ + solutions/       in-session practice (★ warm-up, ★★ core, ★★★ stretch)
  take-home/         starter with the brief at the top (for him), solution/ (for you)
```

## Setup (his laptop)
- Python 3.12+, VS Code + Python extension.
- Copy `Student-Copy/` to his laptop. In `Student-Copy/Python/` run `setup_venv_mac.sh` (or `setup_venv_windows.bat`) → `.venv` with pygame, pytest, requests, matplotlib. Select `.venv` as the interpreter.
- Everything runs in that venv; capstone (P40) gets its own. `.venv` goes in `.gitignore`.
- Stage 4: Git + GitHub account (he's 13 – parent sets it up).

## Session format
| Min | What |
|---|---|
| 0–15 | Review take-home (he demos; you code-review) + 3 recap Qs (slide 2) |
| 15–50 | Teach from slides, live-coding. Stop at *Your turn*. One in-session exercise |
| 50–60 | Start the next take-home together: read the brief, get milestone 1 running |

⭐ Project sessions: 15 review · 10 plan on paper · 30 build M1–M2 · 5 agree take-home milestones.

## Tips
- P01 ex3 is a diagnostic: if he does Q4–5, run P02–P06 at double speed.
- Predict-then-run, always. He types; you hint.
- Checkpoints: `stage1–3_checkpoint` exercises in P10, P20, P30 – revisit weak spots before moving on.
- Missed take-home → do M1–M2 together in the review slot; if it keeps happening, drop stretch goals.
- Let him pick themes (words, worlds, games). Extra builds: project bank below.
- Log sessions in `Progress-Tracker.xlsx`.

## Project bank (extra builds)
- **After Stage 1:** dice poker · times-table trainer with streaks · ASCII animation (`time.sleep` frames) · binary guessing game
- **After Stage 2:** spending tracker (CSV + text bar charts) · Battleships vs computer · turtle Spirograph · creature database (JSON) · Game of Life
- **After Stage 3:** maze generator (DFS) + solver (BFS) · Sudoku backtracker · Huffman compression · unbeatable noughts & crosses (minimax)
- **After Stage 4:** Flappy clone · Snake (body = deque) · weather dashboard + matplotlib · rule-based chatbot with JSON memory · tile-map platformer

## Syllabus

**Stage 1 · Foundations**

| # | Lesson | Covers |
|---|---|---|
| P01 | Hello, Python | setup, print, comments, errors, diagnostic |
| P02 | Variables, Types and Input | variables, int/float/str/bool, input, casting, f-strings |
| P03 | Maths and Operators | operators, // %, **, precedence, math, float error |
| P04 | Making Decisions | if/elif/else, comparisons, and/or/not |
| P05 | While Loops | while, counters, totals, validation, break |
| P06 | For Loops and range() | for, range, strings as sequences, nested loops |
| P07 | ⭐ Project – Higher or Lower | pseudocode, random, milestone building |
| P08 | Strings in Depth | indexing, slicing, string methods, immutability, ord/chr |
| P09 | Lists | lists, append/pop, enumerate, references, 2D lists |
| P10 | ⭐ Project – Hangman | decomposition; Stage 1 checkpoint |

**Stage 2 · Building Blocks**

| # | Lesson | Covers |
|---|---|---|
| P11 | Functions | def, parameters, return, procedure vs function |
| P12 | Functions II – Scope and Design | scope, defaults, docstrings, type hints, main() |
| P13 | Errors, Debugging and Exceptions | error types, tracebacks, debugger, try/except |
| P14 | Dictionaries | dicts, .get, .items, counting pattern |
| P15 | Tuples, Sets and Nested Data | tuples, sets, list of dicts, lambda/comprehensions |
| P16 | Files and CSV | text files, modes, with, CSV |
| P17 | Modules and Libraries | imports, random/time/datetime, own modules, pip + venv |
| P18 | ⭐ Project – Quiz Master | top-down design, CSV data, leaderboard |
| P19 | Turtle Graphics | turtle, polygons, events, recursion preview |
| P20 | ⭐ Project – Text Adventure Engine | data-driven design, parsing, JSON save; Stage 2 checkpoint |

**Stage 3 · Computer Science Theory**

| # | Lesson | Covers |
|---|---|---|
| P21 | Binary, Hex and Data Representation | binary, hex, overflow, units, images, sound |
| P22 | Logic Gates and Boolean Algebra | gates, truth tables, NAND, adders, De Morgan |
| P23 | Algorithms, Pseudocode and Flowcharts | computational thinking, pseudocode, flowcharts, trace tables |
| P24 | Searching Algorithms | linear vs binary search |
| P25 | Sorting I – Bubble and Insertion Sort | bubble sort, insertion sort |
| P26 | Recursion | base/recursive case, call stack, memoisation |
| P27 | Sorting II – Merge Sort and Quicksort | merge sort, quicksort, divide & conquer |
| P28 | Big-O and Efficiency | Big-O, measuring, sets vs lists |
| P29 | Stacks and Queues | stacks, queues, deque, circular queue |
| P30 | ⭐ Project – Sorting Visualiser | generators (yield), animation; Stage 3 checkpoint |

**Stage 4 · Objects and Real Programs**

| # | Lesson | Covers |
|---|---|---|
| P31 | Classes and Objects | classes, objects, __init__, self |
| P32 | Encapsulation and Special Methods | encapsulation, @property, dunder methods, class attributes |
| P33 | Inheritance and Polymorphism | inheritance, super(), polymorphism, composition |
| P34 | Testing and Robust Code | test data, assert, pytest, TDD, validation |
| P35 | Pygame I – The Game Loop | game loop, coordinates, drawing, animation |
| P36 | Pygame II – Input, Sprites and Collisions | input, sprites, groups, collisions, states |
| P37 | ⭐ Project – Arcade Game | game design, game feel, playtesting |
| P38 | Trees and Graphs | BSTs, traversals, graphs, BFS/DFS |
| P39 | JSON, APIs and the Internet | JSON, HTTP, requests, APIs, errors |
| P40 | ⭐ Project – Git and the Python Capstone | Git/GitHub, SDLC, capstone |

## Lesson plans
Full per-lesson plans (timings, answers, notes) are in each folder's `lesson-plan.md`. At a glance:

**Stage 1 · Foundations**

| # | In-session (pick one) | Take-home |
|---|---|---|
| P01 | ★ Name card · ★ ASCII art · ★★ Diagnostic challenges | All About Me poster (~1 hour) |
| P02 | ★ Age calculator · ★★ Bill splitter · ★★★ Swap two variables | RPG Character Creator (1–2 h) |
| P03 | ★ Circle calculator · ★★ Digit splitter · ★★★ Quadratic solver | Savings Goal Calculator (1–2 h) |
| P04 | ★★ Leap year checker · ★ Theme park ride · ★★★ Quadratic solver 2.0 | Choose-Your-Path Story (1–2 h) |
| P05 | ★ Times table · ★★ Password checker · ★★★ The Collatz conjecture | Dice Race to 50 (1–2 h) |
| P06 | ★ FizzBuzz · ★★ Prime finder · ★★★ Chessboard | Pattern Studio (1–2 h) |
| P07 | ★★ Higher or Lower – full game · ★★★ Reverse mode: computer guesses | Finish Higher or Lower (1–2 h) |
| P08 | ★ Initials and username · ★★ Caesar cipher · ★★★ Sentence analyser | Secret Agent Toolkit (1–2 h) |
| P09 | ★ Class test stats · ★★ Do it without built-ins · ★★★ Noughts and crosses board | Playlist Manager (1–2 h) |
| P10 | ★★ Hangman – full game · ★★ Stage 1 checkpoint | Hangman Deluxe (1–2 h) |

**Stage 2 · Building Blocks**

| # | In-session (pick one) | Take-home |
|---|---|---|
| P11 | ★ Unit converter library · ★★ is_prime and friends · ★★★ Dice simulator | Casino Night: Blackjack (1–2 h) |
| P12 | ★ Input helpers module · ★★ Stats functions · ★★★ ATM simulator | Refactor the Mess (1–2 h) |
| P13 | ★★ Bug hunt · ★★ Crash-proof calculator · ★★★ Trace table challenge | Crash-Proof Tuck Shop (1–2 h) |
| P14 | ★ Phone book · ★★ Letter frequency · ★★★ Morse code translator | Top Trumps (1–2 h) |
| P15 | ★ Unique words · ★★ Gradebook · ★★★ RPG inventory | Movie Night Planner (1–2 h) |
| P16 | ★ Journal app · ★★ Weather data analysis · ★★★ Flashcard revision app | Habit Tracker (1–2 h) |
| P17 | ★ Password generator · ★★ Birthday facts · ★★★ Estimate π with random darts | Typing Speed Test (1–2 h) |
| P18 | ★★ Quiz Master – full game | Quiz Master Content (1–2 h) |
| P19 | ★ Shape library · ★★ Etch-a-Sketch · ★★★ Recursive fractal tree | Generative Art Gallery (1–2 h) |
| P20 | ★★ Text adventure – full game · ★★ Stage 2 checkpoint | Write Your World (2 h (over 2 gaps if needed)) |

**Stage 3 · Computer Science Theory**

| # | In-session (pick one) | Take-home |
|---|---|---|
| P21 | ★ Base converter · ★★ Binary adder · ★★★ File size calculator + bitmap | Binary Blitz (1–2 h) |
| P22 | ★★ Truth table generator · ★★ Everything from NAND · ★★★ Build an 8-bit adder from gates | Circuit Simulator (1–2 h) |
| P23 | ★ Pseudocode → Python · ★★ Trace table puzzles · ★★★ Design an algorithm: change machine | Check-Digit Detective (1–2 h) |
| P24 | ★★ Race them · ★★ Search variants · ★★★ Dictionary lookup | Search Showdown (1–2 h) |
| P25 | ★ Sort variations · ★★ Count the work · ★★★ Cocktail shaker sort | Leaderboard Sorter (1–2 h) |
| P26 | ★★ Fibonacci – the slow way and the fast way · ★★ Recursive toolkit · ★★★ Towers of Hanoi | Recursion Puzzle Pack (1–2 h) |
| P27 | ★★ Sort race · ★★ Merge practice · ★★★ In-place quicksort | Big Sort (1–2 h) |
| P28 | ★★ Plot the growth · ★★ Classify and improve · ★★★ Two-sum challenge | Speed Lab Report (1–2 h) |
| P29 | ★★ Build your own Stack and Queue · ★★ Reverse Polish calculator · ★★★ Circular queue | Browser History (1–2 h) |
| P30 | ★★ Sorting visualiser – full program · ★★ Stage 3 checkpoint | Visualiser Upgrades (1–2 h) |

**Stage 4 · Objects and Real Programs**

| # | In-session (pick one) | Take-home |
|---|---|---|
| P31 | ★ Rectangle class · ★★ Stack and Queue as classes · ★★★ RPG battle | Virtual Pet (1–2 h) |
| P32 | ★★ Fraction class · ★★ Deck of cards · ★★★ Bulletproof bank account | Playlist Classes (1–2 h) |
| P33 | ★ Vehicle hierarchy · ★★ Drawable shapes · ★★★ Zoo simulator | Monster Battle Arena (1–2 h) |
| P34 | ★★ Test-driven: password validator · ★★ Test your sorts · ★★★ Robust sign-up form | Bug Bounty (1–2 h) |
| P35 | ★ Draw a scene · ★★ Ball class + gravity · ★★★ 3D starfield | Screensaver (1–2 h) |
| P36 | ★ Coin collector · ★★ Dodge! with sprites and states · ★★★ Breakout | Pong (2 h) |
| P37 | ★★★ Space shooter – reference game | Keep Building Your Game (2 h per gap (2–3 gaps)) |
| P38 | ★★ BST class · ★★ Maze solver · ★★★ Six degrees of separation | Folder Tree Explorer (1–2 h) |
| P39 | ★★ Weather app · ★★ Pokédex · ★★★ Live trivia game | Personal Dashboard (1–2 h) |
| P40 | ★ Git practice · ★★★ Capstone project template | Capstone Sprints (2 h per gap (3–5 gaps)) |

## GCSE coverage
| Area | Lessons |
|---|---|
| Variables, types, casting, operators (DIV/MOD) | P02–P03 |
| Selection, iteration, nesting | P04–P06 |
| Strings, ASCII/Unicode | P08, P21 |
| Arrays/lists, 2D, records | P09, P15 |
| Subroutines, parameters, scope | P11–P12 |
| Files, validation, defensive design | P13, P16, P34 |
| Errors (syntax/runtime/logic), testing, test data | P13, P34 |
| Pseudocode, flowcharts, trace tables, computational thinking | P23 |
| Linear/binary search; bubble/insertion/merge sort | P24, P25, P27 |
| Binary, hex, overflow, units, images, sound | P21 |
| Logic gates, truth tables | P22 |
| Compilers vs interpreters | P01 (and C01) |
| A-level+: recursion, quicksort, Big-O, stacks/queues, trees, graphs/BFS, OOP | P26–P29, P31–P33, P38 |
