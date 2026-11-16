# P32 · Encapsulation and Special Methods

**Stage:** Objects and Real Programs  
**Session type:** Lesson (≈60 min)  
**Slides:** `P32-Encapsulation-and-Special-Methods.pptx`

_Protecting your objects' data and making them behave like built-in types_

## Learning goals
- Explain encapsulation and use "private" attributes
- Write getters/setters with @property
- Use __str__, __repr__, __eq__, __lt__ and __len__
- Use class attributes vs instance attributes

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's the difference between an attribute and a method?  
   **Answer:** Attribute = data on an object; method = function on an object
2. What does __init__ do?  
   **Answer:** Sets up a new object's attributes when it's created (the constructor)
3. What is `self`?  
   **Answer:** The particular object the method was called on

## Slide outline & tutor notes

**3. Encapsulation**  
Python trusts programmers ("we're all adults here"). C# has real `private` enforced by the compiler – we'll see it in C08.

**4. @property: smart attributes**

**5. __str__ and __repr__**

**6. Operators on your objects**

**7. Class attributes**

**8. Make it Pythonic**

**9. Dunder quiz**
- Which method does `print(obj)` use? → **__str__**
- Which method makes `a + b` work? → **__add__**
- What does a leading underscore like `_score` signal? → **It's private – outside code shouldn't use it directly**
- What's a class attribute? → **A value shared by every object of the class**
- What does @property let you do? → **Run code (e.g. validation) when an attribute is read or set, while still using attribute syntax**

## 🏠 Take-home project: Playlist Classes
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Rebuild your P09 playlist with proper classes that behave like built-in types using special (dunder) methods.

**Milestones**
1. `Song` class: title, artist, seconds. `__str__` shows "Title – Artist (3:25)"; `__eq__` compares title + artist
2. `length` is a `@property` that formats seconds as m:ss
3. `Playlist` class holding a list of songs: `add()`, `remove()`, `shuffle()`
4. Special methods: `__len__` (number of songs), `__str__` (numbered list + total time), `__contains__` (so `song in playlist` works), `__add__` (two playlists → a new combined one)
5. Test every method with a few lines of code at the bottom

**Stretch:** Make Playlist iterable (`__iter__`) and sortable by length with `__lt__` on Song.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Fraction class  (★★☆ core)
File: `exercises/ex1_fraction.py`

Write a Fraction class that stores a numerator and denominator in lowest terms (use math.gcd). Support +, -, *, ==, < and printing as "3/4". Check: 1/2 + 1/3 = 5/6.

### Deck of cards  (★★☆ core)
File: `exercises/ex2_deck.py`

Make Card and Deck classes. Deck builds all 52 cards, can `shuffle()`, `deal(n)` and has `__len__`. Deal two 5-card hands and print them. Cards should compare by rank so you can find each hand's highest card.

### Bulletproof bank account  (★★★ stretch)
File: `exercises/ex3_safe_account.py`

Rewrite BankAccount so balance is read-only from outside (a property with no setter), every transaction is recorded in a private history list, and there's a `statement()` method. Add a class attribute for the interest rate and an `add_interest()` method. Try to break it from outside!

## Optional extras (if he wants more)
- Add `__str__` and at least one operator to the class you made for homework last time
- Read about the "four pillars of OOP": encapsulation, abstraction, inheritance, polymorphism – we've done one, the next lesson covers two more
