# P31 · Classes and Objects

**Stage:** Objects and Real Programs  
**Session type:** Lesson (≈60 min)  
**Slides:** `P31-Classes-and-Objects.pptx`

_Object-oriented programming – bundling data and behaviour together_

## Learning goals
- Explain classes, objects, attributes and methods
- Write a class with __init__ and self
- Create several objects from one class
- Model real things (a bank account, a pet, a game character) as classes

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `yield` do in a function?  
   **Answer:** Pauses it and hands back a value; it carries on from there next time
2. Which sort was fastest in your visualiser and why?  
   **Answer:** Merge/quick – O(n log n) vs O(n²)
3. What's a generator?  
   **Answer:** A function that produces values one at a time using yield

## Slide outline & tutor notes

**3. Why objects?**  
C#, Java and most game engines (Unity!) are built entirely around classes. This lesson is the bridge to Stage 5.

**4. Your first class**

**5. What is self?**  
Common bug: forgetting self in the def line, or writing `name` instead of `self.name` inside a method.

**6. A bank account**

**7. Vocabulary check**

**8. Make a class**

**9. OOP quiz**
- What's the difference between a class and an object? → **A class is the blueprint; an object is an instance built from it**
- What's `__init__` for? → **Setting up a new object's attributes when it's created**
- In `rex.bark()`, what is `self` inside bark? → **rex**
- Is `"hello".upper()` a function or a method? → **A method – it belongs to the str class**
- How many objects: `a = Dog("A","x")`, `b = a`? → **One – b is another name for the same object**

## 🏠 Take-home project: Virtual Pet
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A Tamagotchi-style pet as a class. Time passes between your actions, so you have to keep it happy!

**Milestones**
1. A `Pet` class with name, hunger, happiness and energy (0–10) and an `age` in turns
2. Methods: `feed()`, `play()`, `sleep()`, `tick()` (one turn passing: hunger up, happiness and energy down) and `status()`
3. Keep values between 0 and 10 with `max`/`min`
4. `is_alive()` – the pet runs away if hunger hits 10 or happiness hits 0
5. A game loop: show status, choose an action, then `tick()` – how many turns can you keep it going?

**Stretch:** Own two pets at once (a list of Pet objects); each action asks which pet.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Rectangle class  (★☆☆ warm-up)
File: `exercises/ex1_rectangle.py`

Write a Rectangle class with width and height, methods `area()`, `perimeter()`, `is_square()` and `scale(factor)`. Make a list of 5 random rectangles and print the biggest.

### Stack and Queue as classes  (★★☆ core)
File: `exercises/ex2_stack_class.py`

Turn your Stack and Queue functions from P29 into classes with push/pop/peek/is_empty/size (and enqueue/dequeue). Use them to redo the bracket checker.

### RPG battle  (★★★ stretch)
File: `exercises/ex3_rpg_fighters.py`

Make a `Fighter` class: name, hp, attack, defence. Methods: `is_alive()`, `take_damage(n)` (reduced by defence, minimum 1) and `attack_target(other)` with a random 10% critical hit for double damage. Run a turn-by-turn battle between two fighters with a commentary.

## Optional extras (if he wants more)
- Model something you're into as a class – a football player, a Pokémon-style creature, a car – with at least 3 attributes and 3 methods
- Find 3 methods on Python's list class you've never used (`help(list)`)
