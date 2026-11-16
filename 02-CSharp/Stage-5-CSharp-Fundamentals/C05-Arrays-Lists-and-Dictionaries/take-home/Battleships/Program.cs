// TAKE-HOME PROJECT: Battleships
// After lesson C05 (Arrays, Lists and Dictionaries) - about 2 hours, in chunks over the next few days.
//
// Single-player Battleships against a hidden computer fleet, using 2D arrays and
// collections.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. An 8×8 char[,] board for the hidden ships and another for what the player has seen
//   [ ] 2. Place 3 ships (lengths 4, 3, 2) randomly, horizontally or vertically, without
//          overlapping or going off the board
//   [ ] 3. The player has 25 shots: type a coordinate like C5 – parse the letter and number,
//          re-ask on bad input or repeated shots
//   [ ] 4. Show X for hits, o for misses; announce "Sunk!" when a whole ship is hit (track
//          each ship's cells in a List<(int, int)>)
//   [ ] 5. Win when every ship is sunk; lose when out of shots and reveal the fleet
//
// Stretch: Make it two-player against a computer that shoots back, hunting around its
// hits.
//
// Bring it to the next session - working or stuck, both are fine.

const int Size = 8;
char[,] ships = new char[Size, Size];
char[,] seen = new char[Size, Size];
