# C15 · Files and JSON

**Stage:** CSharp Beyond the Basics  
**Session type:** Lesson (≈60 min)  
**Slides:** `C15-Files-and-JSON.pptx`

_Saving and loading game data with System.IO and System.Text.Json_

## Learning goals
- Read and write text files with File and StreamReader/StreamWriter
- Use `using` to dispose resources safely
- Serialise objects to JSON and back with System.Text.Json
- Build a save/load system for a game

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `nums.Where(n => n > 5)` return?  
   **Answer:** The items greater than 5 (a lazy sequence)
2. Func vs Action?  
   **Answer:** Func returns a value; Action doesn't
3. What does `.ToList()` do to a LINQ query?  
   **Answer:** Runs it immediately and stores the results in a list

## Slide outline & tutor notes

**3. The File class: one-liners**

**4. Streams and using**

**5. JSON: objects ↔ text**

**6. CSV into records**

**7. What gets saved?**  
Good design: don't serialise your whole Game object – make a SaveData record that captures just the state, and methods to convert to and from it.

**8. Save the dungeon**

**9. Files quiz**
- Python's `with open(...)` in C#? → **using var x = new StreamReader(...) (or a using block)**
- Which method turns an object into JSON text? → **JsonSerializer.Serialize**
- What's `Path.Combine` for? → **Building file paths that work on any operating system**
- Are private fields saved by System.Text.Json? → **No – only public properties by default**
- Which exception for bad JSON? → **JsonException**

## 🏠 Take-home project: Habit Tracker 2.0
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Rebuild your Python habit tracker in C#, saving everything as JSON.

**Milestones**
1. Records: `Habit(string Name, List<DateOnly> DoneOn)` and `TrackerData(int Version, List<Habit> Habits)`
2. Load `habits.json` at start (empty if missing; catch `JsonException` and back up a corrupt file instead of crashing)
3. Menu: add a habit, tick off today, show report, quit – save after every change
4. Report: for each habit, total days done and the current streak (consecutive days up to today)
5. Show the last 14 days as a row of ✓ and · for each habit

**Stretch:** Use your `SaveManager<T>` from the lesson's stretch exercise to handle the saving.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Journal app  (★☆☆ warm-up)
File: `exercises/ex1_journal/Program.cs`

Port P16's journal: append a dated entry to journal.txt each run, then print the last 3 entries using File.ReadAllLines and LINQ's TakeLast.

### Contacts app with JSON  (★★☆ core)
File: `exercises/ex2_contacts_json/Program.cs`

A contacts manager (add, search by partial name, delete, list) that stores a `List<Contact>` record (Name, Phone, Email, Birthday as DateOnly) in contacts.json, loaded at start and saved after every change. Show upcoming birthdays in the next 30 days.

### Versioned save system  (★★★ stretch)
File: `exercises/ex3_save_system/Program.cs`

Write a generic `SaveManager<T>` with Save(slot, data), Load(slot) returning T?, ListSlots() and Delete(slot), storing files in a "saves" folder. Wrap data in an envelope record with a Version and Timestamp. Handle corrupt files gracefully. Test it with a GameState record.

## Optional extras (if he wants more)
- Add save/load to your Console Arcade or Dungeon Crawler
- Open a .json save file in VS Code and edit it by hand – give yourself 9999 gold. That's why games encrypt saves!
