// TAKE-HOME PROJECT: Generic Leaderboard
// After lesson C13 (Generics and Collections) - about 1–2 hours, in chunks over the next few days.
//
// Write a reusable, generic leaderboard class that works for any kind of entry – then use
// it for two different games.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. class Leaderboard<T> where T : IComparable<T> holding at most N entries (N set in
//          the constructor)
//   [ ] 2. Add(T entry) keeps it sorted best-first and drops the worst if it's over N;
//          returns the position (or -1 if it didn't make it)
//   [ ] 3. Implement IEnumerable<T> (or just expose IReadOnlyList<T> Entries) so you can
//          foreach over it
//   [ ] 4. Two record types implementing IComparable<T>: TimeEntry (fastest wins) and
//          ScoreEntry (highest wins, ties by name)
//   [ ] 5. Fill one board with 20 random race times and one with 20 random scores; print the
//          top 5 of each
//
// Stretch: Add a generic Top<T>(IEnumerable<T> items, int n, Func<T, double> score) method
// that doesn't need IComparable at all.
//
// Bring it to the next session - working or stuck, both are fine.

Console.WriteLine("Leaderboards – create two boards and fill them here");

public class Leaderboard<T> where T : IComparable<T>
{
}
