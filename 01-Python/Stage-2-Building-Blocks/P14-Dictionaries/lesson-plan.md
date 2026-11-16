# P14 · Dictionaries

**Stage:** Building Blocks  
**Session type:** Lesson (≈60 min)  
**Slides:** `P14-Dictionaries.pptx`

_Look things up by name, not by position – key → value pairs_

## Learning goals
- Create dictionaries and read, add, update and delete entries
- Loop over keys, values and items
- Use .get() to avoid KeyErrors
- Count things with a dictionary

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Name the three kinds of error  
   **Answer:** Syntax, runtime, logic
2. Which exception does `int("hi")` raise?  
   **Answer:** ValueError
3. What does `finally` do?  
   **Answer:** Runs whether or not an exception happened

## Slide outline & tutor notes

**3. What's a dictionary?**  
Hash tables come back in A-level. For now: "Python does clever maths on the key to jump straight to it".

**4. Creating and using**

**5. Looping**

**6. The counting pattern**  
Also show sorting by count: `sorted(counts.items(), key=lambda kv: kv[1], reverse=True)` – just as a teaser for lambdas (C14 in C#).

**7. List or dictionary?**

**8. Emoji translator**

**9. Predict it**
- `d = {"a": 1}` then `d["b"] = 2` – what's `len(d)`? → **2**
- `d = {"x": 5}` – what's `d.get("y", 9)`? → **9**
- `d = {"a": 1, "a": 2}` – what's `d["a"]`? → **2 – keys are unique, the last one wins**
- Can a list be a dictionary key? → **No – keys must be immutable (a tuple is fine)**
- `{"a": 1, "b": 2}.items()` gives? → **pairs ('a', 1), ('b', 2)**

## 🏠 Take-home project: Top Trumps
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Make a Top Trumps card game against the computer. Each card is a dictionary of stats.

**Milestones**
1. Make at least 10 cards as dictionaries, e.g. `{"name": "Dragon", "power": 95, "speed": 60, "magic": 88}` (invent your own theme)
2. Shuffle and deal them into two lists: your hand and the computer's
3. Each round: show your top card, you choose a stat, compare with the computer's top card
4. The winner takes both cards (put them at the bottom of their hand). Draws: both cards go back
5. Play until someone has all the cards (or 20 rounds) – then say who won

**Stretch:** When the computer wins a round it chooses the stat next time – make it choose its best stat.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Phone book  (★☆☆ warm-up)
File: `exercises/ex1_phone_book.py`

A menu-driven phone book: add a contact, look one up, delete one, list all (sorted by name), quit.

### Letter frequency  (★★☆ core)
File: `exercises/ex2_letter_freq.py`

Count how often each letter appears in a piece of text (ignore case and non-letters). Print the top 5 letters with bar charts. English text usually starts e, t, a, o… does yours?

### Morse code translator  (★★★ stretch)
File: `exercises/ex3_morse.py`

Build a dictionary for A–Z and 0–9 in Morse code. Translate text → Morse (letters separated by spaces, words by " / "). Then build the reverse dictionary automatically and translate Morse → text.

## Optional extras (if he wants more)
- Make a "word of the day" vocab quiz: a dictionary of 10 words → meanings; ask 5 random ones and score the player
- Find out what happens if you loop over a dictionary and delete from it at the same time (try it!)
