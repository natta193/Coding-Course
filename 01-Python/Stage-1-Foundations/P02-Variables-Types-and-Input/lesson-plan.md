# P02 · Variables, Types and Input

**Stage:** Foundations  
**Session type:** Lesson (≈60 min)  
**Slides:** `P02-Variables-Types-and-Input.pptx`

_Storing data, asking the user questions, and why "5" isn't 5_

## Learning goals
- Create and update variables with good names
- Know the four basic types: int, float, str, bool
- Get input from the user and convert it with int() / float()
- Format output neatly with f-strings

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `print(2 * 8)` show?  
   **Answer:** 16
2. What's the difference between `print(5)` and `print("5")`?  
   **Answer:** Nothing visible – but one is a number and one is text
3. What is a SyntaxError?  
   **Answer:** A grammar mistake in the code, e.g. a missing bracket or quote

## Slide outline & tutor notes

**3. Variables are labelled boxes**  
Draw boxes on paper. Ask: after `a = 5`, `b = a`, `a = 7` – what is b? (5). This catches a classic misconception.

**4. Variables in action**

**5. The four basic data types**  
GCSE also mentions char (single character) – Python has no separate char type, a char is just a str of length 1. Mention for exam awareness.

**6. input() always gives you a string**  
Run the crashing version first and read the TypeError together: "can only concatenate str (not "int") to str". This is the #1 beginner bug.

**7. f-strings: the neat way to print**

**8. Joining text: + vs f-strings**

**9. Mad Libs**  
Let him pick the story – humour makes it stick.

**10. Predict the output**
- `x = 3` then `x = x * 2` then `print(x)` → **6**
- `type("3.5")` → **str – it's in quotes**
- `int("7") + 1` → **8**
- `"7" + "1"` → **"71" – joining strings, not adding**
- `f"{10/4}"` → **2.5**
- `int(3.9)` → **3 – int() chops off the decimal, it doesn't round**

## 🏠 Take-home project: RPG Character Creator
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Build a character creator for an imaginary role-playing game. Ask the player questions, work out their stats with maths, and print a beautiful character sheet using f-strings.

**Milestones**
1. Ask for a name, a class (warrior / mage / rogue – just type it for now) and age
2. Ask for 3 numbers from 1–10: strength, smarts, speed. Store each in a variable
3. Calculate: health = strength × 10 + 50, mana = smarts × 8, dodge chance = speed × 3 (%)
4. Print a character sheet with a border, lined-up labels and the calculated stats
5. Add a "power level" = the average of the three stats, shown to 1 decimal place

**Stretch:** Ask how many gold coins they start with and how much a sword costs; print how many swords they can buy and how much change is left (use // and %).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Age calculator  (★☆☆ warm-up)
File: `exercises/ex1_age_in_days.py`

Ask for the user's age in years. Print how many days, hours and minutes old they are (roughly – ignore leap years).

### Bill splitter  (★★☆ core)
File: `exercises/ex2_bill_splitter.py`

Ask for the total bill, the tip percentage and how many people. Print what each person pays to 2 decimal places.

### Swap two variables  (★★★ stretch)
File: `exercises/ex3_swap.py`

Make `a = 5` and `b = 9`. Swap their values so a is 9 and b is 5 – first using a third variable, then the Python one-liner `a, b = b, a`. Explain why `a = b` then `b = a` doesn't work.

## Optional extras (if he wants more)
- Write a program that asks for a temperature in °C and converts it to °F (F = C × 9/5 + 32)
- Make a "profile card" program that asks 5 questions and prints a neat summary with f-strings
