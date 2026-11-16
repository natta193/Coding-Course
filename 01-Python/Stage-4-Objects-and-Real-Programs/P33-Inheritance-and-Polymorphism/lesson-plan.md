# P33 · Inheritance and Polymorphism

**Stage:** Objects and Real Programs  
**Session type:** Lesson (≈60 min)  
**Slides:** `P33-Inheritance-and-Polymorphism.pptx`

_Building families of classes that share code but behave differently_

## Learning goals
- Create subclasses that inherit from a parent class
- Override methods and call the parent with super()
- Use polymorphism to treat different objects the same way
- Choose between inheritance ("is a") and composition ("has a")

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does encapsulation mean?  
   **Answer:** Bundling data with methods and controlling access to the data
2. What does `__str__` do?  
   **Answer:** Defines what print() shows for an object
3. What's the difference between a class attribute and an instance attribute?  
   **Answer:** Class attribute is shared by all objects; instance attribute belongs to one object

## Slide outline & tutor notes

**3. Inheritance: "is a"**  
Draw a class diagram: Animal at top, Dog and Cat below with arrows pointing up. UML-style class diagrams appear at A-level.

**4. A class family**

**5. super(): extending the parent**

**6. Polymorphism: many forms**

**7. Polymorphism in action**

**8. Inheritance vs composition**  
Unity is heavily composition-based (GameObjects have Components). Good to plant now before C18.

**9. Character classes**

**10. OOP pillars quiz**
- In `class B(A):`, which is the parent? → **A**
- What does `super().__init__(...)` do? → **Calls the parent class's constructor**
- What is overriding? → **A subclass providing its own version of a method the parent already has**
- Car and Engine – inheritance or composition? → **Composition – a car HAS an engine**
- Name the four pillars of OOP → **Encapsulation, abstraction, inheritance, polymorphism**

## 🏠 Take-home project: Monster Battle Arena
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A tournament of monsters built with inheritance and polymorphism.

**Milestones**
1. A base `Monster` class: name, hp, attack, `take_damage()`, `is_alive()`, `act(opponent)` (a normal attack) and `__str__`
2. At least 4 subclasses that override `act()` with a special move: e.g. `FireDragon` (burn damage over time), `Slime` (splits/heals), `Vampire` (steals hp), `Turtle` (blocks every other hit by overriding `take_damage`)
3. Use `super()` in every subclass constructor
4. `battle(a, b)` runs a fight turn by turn and returns the winner
5. A round-robin tournament: every monster fights every other once; print a league table of wins

**Stretch:** Add a `Trainer` class that HAS a team of 3 monsters (composition) and fight trainer vs trainer.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Vehicle hierarchy  (★☆☆ warm-up)
File: `exercises/ex1_vehicles.py`

Make Vehicle (make, model, wheels, `describe()`), then Car, Motorbike and Lorry subclasses. Lorry adds a cargo capacity and overrides describe. Store a mixed list and describe them all.

### Drawable shapes  (★★☆ core)
File: `exercises/ex2_shapes_turtle.py`

Make an abstract Shape with x, y, colour and `area()`/`draw(t)` methods. Subclasses Circle, Rect and Triangle draw themselves with turtle. Generate 20 random shapes, draw them all, and print the total area.

### Zoo simulator  (★★★ stretch)
File: `exercises/ex3_zoo.py`

Animal base class with hunger and `daily_needs()`. At least 4 species with different food, noise and a `special()` behaviour. A Zoo class **has** a list of enclosures (composition), each holding animals. Simulate 7 days: random events, feeding, and a daily report.

## Optional extras (if he wants more)
- Draw a class diagram for your zoo or character classes: boxes with attributes and methods, arrows for inheritance
- Think about a game you'd like to build in Pygame next – what classes would it need?
