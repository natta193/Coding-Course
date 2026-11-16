# P15 · Tuples, Sets and Nested Data

**Stage:** Building Blocks  
**Session type:** Lesson (≈60 min)  
**Slides:** `P15-Tuples-Sets-and-Nested-Data.pptx`

_Picking the right container, and modelling real things with lists of dictionaries_

## Learning goals
- Use tuples for fixed groups of values and unpack them
- Use sets for uniqueness and set maths (union, intersection)
- Build and navigate nested structures like a list of dictionaries
- Choose the right data structure for a job

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How do you safely read a key that might not exist?  
   **Answer:** d.get(key, default)
2. How do you loop over keys and values together?  
   **Answer:** for k, v in d.items():
3. What's the counting pattern?  
   **Answer:** counts[x] = counts.get(x, 0) + 1

## Slide outline & tutor notes

**3. Tuples: lists you can't change**

**4. Sets: no duplicates allowed**

**5. Choosing a data structure**

**6. Nested data: list of dictionaries**  
Read `students[2]["scores"][0]` left to right: list item 2 → its "scores" → item 0. Get him to say it aloud.

**7. Sorting complex data**  
Lambdas and comprehensions are optional power tools. Don't force them – but he's smart, he'll love them.

**8. Movie database**

**9. Which structure?**
- Storing a chess board's 64 squares → **2D list (list of lists)**
- The days of the week (never change) → **tuple**
- Usernames already taken on a website → **set – fast "is it taken?" check**
- A player's inventory: item name → quantity → **dictionary**
- What does `len({1, 1, 2, 2, 3})` give? → **3**

## 🏠 Take-home project: Movie Night Planner
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Help a group of friends choose a film. Each movie is a dictionary inside a list, and sets work out what everyone can agree on.

**Milestones**
1. Make a list of at least 8 movies: title, year, age rating (as a number), length in minutes, and a list of genres
2. Ask how many friends; for each, ask their age and which genres they like (comma-separated) – store each friend's genres as a **set**
3. Find the genres EVERYONE likes (set intersection) and the youngest friend's age
4. Shortlist movies suitable for the youngest friend that have at least one shared genre
5. Print the shortlist sorted by length, and pick a random winner

**Stretch:** Let each friend vote for one film on the shortlist; count votes with a dictionary and announce the winner (random tiebreak).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Unique words  (★☆☆ warm-up)
File: `exercises/ex1_unique_words.py`

Ask for two sentences. Print the words they have in common, the words only in the first, and how many unique words there are altogether. Use sets.

### Gradebook  (★★☆ core)
File: `exercises/ex2_gradebook.py`

Using the `students` list of dictionaries from the slides: print a report card for each student (average + grade), the class average, the top student, and every student who improved on every test.

### RPG inventory  (★★★ stretch)
File: `exercises/ex3_inventory.py`

Model a game character as a dictionary: name, hp, gold, and an inventory that's a dictionary of item → {"qty": int, "value": int}. Write functions to pick up an item, sell an item (gain gold), and print the inventory sorted by total value.

## Optional extras (if he wants more)
- Model your favourite game's characters (or football squad) as a list of dictionaries and write 3 queries on it
- Look up the difference between `a.copy()` and `copy.deepcopy(a)` for nested lists
