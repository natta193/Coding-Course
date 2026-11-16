# C08 · Classes, Objects and Properties

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C08-Classes-Objects-and-Properties.pptx`

_OOP the way C# was designed for it – access modifiers, constructors and properties_

## Learning goals
- Write classes with fields, constructors and methods
- Use access modifiers: public and private
- Use properties (get/set, auto-properties, read-only, computed)
- Override ToString and use static members

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How do you read one key press without Enter?  
   **Answer:** Console.ReadKey(true)
2. How do you write a list of lines to a file in one go?  
   **Answer:** File.WriteAllLines(path, lines)
3. Remind me: class vs object?  
   **Answer:** Class = blueprint; object = instance created from it

## Slide outline & tutor notes

**3. A C# class**

**4. Using it**

**5. Access modifiers**

**6. Properties with logic**

**7. Static members**

**8. Bank account**

**9. C# classes quiz**
- What's the default access level for class members? → **private**
- What's a constructor? → **A special method (same name as the class) that sets up a new object**
- `public int X { get; private set; }` – who can change X? → **Only code inside the class**
- What does `override ToString()` change? → **What you see when the object is printed or put in a string**
- How do you call a static method? → **ClassName.Method() – on the class, not an object**

## 🏠 Take-home project: Library System
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Model a school library with classes, properties and encapsulation.

**Milestones**
1. `Book` class: Title, Author, Isbn (read-only), and `IsOnLoan` with a private setter
2. `Member` class: Name, a read-only list of borrowed books (max 3)
3. `Library` class with private lists of books and members; methods `AddBook`, `Join`, `Lend(isbn, memberName)`, `Return(isbn)` – each returns bool and prints why it failed
4. `Search(string text)` finds books by partial title or author
5. A menu loop in top-level code that only talks to the Library – never to the lists directly

**Stretch:** Add due dates (`DateTime.Today.AddDays(14)`) and a "who's overdue?" report.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Rectangle class  (★☆☆ warm-up)
File: `exercises/ex1_rectangle/Program.cs`

Port P31's Rectangle with properties Width and Height (must be positive – throw `ArgumentException` otherwise), computed properties Area, Perimeter and IsSquare, a `Scale` method and ToString.

### Bank account  (★★☆ core)
File: `exercises/ex2_bank_account/Program.cs`

Build the BankAccount from the "Your turn" slide, then make 3 accounts, do some transactions, apply interest to all and print statements.

### Cards and Deck  (★★★ stretch)
File: `exercises/ex3_deck/Program.cs`

Port P32's Card and Deck. Card has Rank and Suit (read-only), a Value property and ToString. Deck has a private List<Card>, Shuffle (Fisher–Yates – write it yourself!), Deal(n) and Count. Deal two hands and find the higher.

## Optional extras (if he wants more)
- Port your P31 Pet (Tamagotchi) class to C# with properties that clamp hunger/happiness to 0–10
- Use the VS Code debugger in C#: set a breakpoint in a method and inspect an object's fields
