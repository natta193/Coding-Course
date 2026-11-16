# C09 · Inheritance, Abstract Classes and Interfaces

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C09-Inheritance-Abstract-Classes-and-Interfaces.pptx`

_Class hierarchies, virtual/override, and contracts with interfaces_

## Learning goals
- Create subclasses with `: Base` and call base constructors
- Use virtual, override and abstract
- Define and implement interfaces
- Use polymorphism with base-class and interface references

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `private` mean?  
   **Answer:** Only code inside the same class can access it
2. Write an auto-property for Name that can only be set inside the class  
   **Answer:** public string Name { get; private set; }
3. What is a static member?  
   **Answer:** One that belongs to the class itself, shared by all objects

## Slide outline & tutor notes

**3. Inheritance in C#**

**4. virtual and override – why so strict?**

**5. Abstract classes**

**6. Interfaces: a contract**  
Unity uses this pattern constantly – e.g. IDamageable on anything that can be hit. Good preview of C18–C20.

**7. Polymorphism**

**8. Abstract class vs interface**

**9. Character classes**  
`is` pattern matching – `if (c is IHealer h)` both tests and casts. Very handy.

**10. Inheritance quiz**
- Python's `super().__init__(name)` in C#? → **: base(name) after the constructor's parameter list**
- What must a parent method be marked so a child can override it? → **virtual (or abstract)**
- Can you write `new Shape()` if Shape is abstract? → **No**
- How many classes can a C# class inherit from? Interfaces? → **One class; any number of interfaces**
- What does `protected` mean? → **Accessible in this class and its subclasses only**

## 🏠 Take-home project: ASCII Shape Painter
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

An abstract Shape class whose subclasses draw themselves onto a text "canvas" – polymorphism you can see.

**Milestones**
1. A `Canvas` class wrapping a `char[,]` (e.g. 40×20) with `Plot(x, y, ch)` (ignore off-canvas points) and `Show()`
2. `abstract class Shape` with X, Y, a fill char, `abstract void Draw(Canvas c)` and `abstract double Area()`
3. Subclasses: `Rect`, `Circle` (plot points where (dx²+dy²) ≤ r²), `Triangle`
4. An `IMovable` interface with `Move(dx, dy)` – implement it on all shapes
5. Put 5 shapes in a `List<Shape>`, draw them all, move them, draw again; print the total area

**Stretch:** Add a `Text` shape that draws a word, and a "scene file" format you read to create shapes.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Vehicle hierarchy  (★☆☆ warm-up)
File: `exercises/ex1_vehicles/Program.cs`

Port P33's vehicles: abstract Vehicle (Make, Model, abstract Wheels, virtual Describe), Car, Motorbike, Lorry (adds Cargo and overrides Describe using `base.Describe()`).

### RPG party  (★★☆ core)
File: `exercises/ex2_rpg_classes/Program.cs`

Build the Character classes from the "Your turn" slide and run a party-vs-monster battle: each round every living hero attacks the monster, the monster attacks a random hero, healers heal the weakest ally.

### Shapes with IComparable  (★★★ stretch)
File: `exercises/ex3_shapes_interface/Program.cs`

Make abstract Shape implement `IComparable<Shape>` (compare by area) so `List<Shape>.Sort()` works. Add Circle, Rectangle and Triangle (Heron's formula). Create 10 random shapes, sort them, print them, and print the total area.

## Optional extras (if he wants more)
- Draw a class diagram of your RPG classes including the interface (dashed arrow for "implements")
- Find 3 interfaces in .NET (hint: IEnumerable, IComparable, IDisposable) and what they promise
