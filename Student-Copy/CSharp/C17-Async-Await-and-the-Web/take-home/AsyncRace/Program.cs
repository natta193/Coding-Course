// TAKE-HOME PROJECT: Async Horse Race
// After lesson C17 (Async, Await and the Web) - about 1–2 hours, in chunks over the next few days.
//
// A console horse race where every horse is its own async task – watch concurrency happen.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. async Task<string> RunHorse(string name, int trackLength, IProgress<(string, int)>
//          progress) – loop: wait a random Task.Delay(50–250ms), move 1 step, report progress
//   [ ] 2. Start 5 horses at once; draw the track on every progress update (SetCursorPosition
//          or just reprint)
//   [ ] 3. Use Task.WhenAny to announce the winner the moment the first horse finishes
//   [ ] 4. Then await Task.WhenAll for the rest and print the finishing order with times
//          (Stopwatch)
//   [ ] 5. Let the player bet on a horse before the race
//
// Stretch: Add a CancellationToken so pressing a key stops the race early ("the race has
// been abandoned!").
//
// Bring it to the next session - working or stuck, both are fine.

using System.Diagnostics;

string[] horses = { "Thunder", "Biscuit", "Comet", "Pickle", "Shadow" };
