// TAKE-HOME PROJECT: The Card Game War
// After lesson C12 (Value Types, References, Enums and Null) - about 1–2 hours, in chunks over the next few days.
//
// Play the classic card game War, modelled with enums, records and value types.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. enum Suit { Clubs, Diamonds, Hearts, Spades } and enum Rank { Two = 2, …, Ace = 14
//          }
//   [ ] 2. record Card(Rank Rank, Suit Suit) with a nice ToString (e.g. "Q♥")
//   [ ] 3. Build and shuffle a 52-card deck with Enum.GetValues; deal into two Queue<Card>
//          hands
//   [ ] 4. Each round both players flip their top card; the higher rank takes both (put them
//          at the back of their queue)
//   [ ] 5. A tie means "war": each puts 3 cards face down and flips another – the winner
//          takes the whole pile. Stop after 1,000 rounds or when someone has no cards
//
// Stretch: Run 1,000 games silently and report the average number of rounds a game takes.
//
// Bring it to the next session - working or stuck, both are fine.

Console.WriteLine("War – build and shuffle the deck here");

public enum Suit { Clubs, Diamonds, Hearts, Spades }
public enum Rank { Two = 2, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace }

public record Card(Rank Rank, Suit Suit);
