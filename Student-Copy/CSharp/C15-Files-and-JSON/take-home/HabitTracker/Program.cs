// TAKE-HOME PROJECT: Habit Tracker 2.0
// After lesson C15 (Files and JSON) - about 1–2 hours, in chunks over the next few days.
//
// Rebuild your Python habit tracker in C#, saving everything as JSON.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. Records: Habit(string Name, List<DateOnly> DoneOn) and TrackerData(int Version,
//          List<Habit> Habits)
//   [ ] 2. Load habits.json at start (empty if missing; catch JsonException and back up a
//          corrupt file instead of crashing)
//   [ ] 3. Menu: add a habit, tick off today, show report, quit – save after every change
//   [ ] 4. Report: for each habit, total days done and the current streak (consecutive days
//          up to today)
//   [ ] 5. Show the last 14 days as a row of ✓ and · for each habit
//
// Stretch: Use your SaveManager<T> from the lesson's stretch exercise to handle the
// saving.
//
// Bring it to the next session - working or stuck, both are fine.

using System.Text.Json;

Console.WriteLine("Habit Tracker – load habits.json here");

public record Habit(string Name, List<DateOnly> DoneOn);
public record TrackerData(int Version, List<Habit> Habits);
