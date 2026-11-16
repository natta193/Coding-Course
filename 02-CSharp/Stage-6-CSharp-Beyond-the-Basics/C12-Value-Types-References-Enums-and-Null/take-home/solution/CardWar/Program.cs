var deck = (from s in Enum.GetValues<Suit>() from r in Enum.GetValues<Rank>() select new Card(r, s)).ToArray();
Random.Shared.Shuffle(deck);
var p1 = new Queue<Card>(deck[..26]);
var p2 = new Queue<Card>(deck[26..]);
int round = 0;

while (p1.Count > 0 && p2.Count > 0 && round < 1000)
{
    round++;
    var pile = new List<Card>();
    Card a, b;
    do
    {
        if (p1.Count == 0 || p2.Count == 0) break;
        a = p1.Dequeue();
        b = p2.Dequeue();
        pile.Add(a);
        pile.Add(b);
        if (a.Rank != b.Rank)
        {
            var winner = a.Rank > b.Rank ? p1 : p2;
            if (round <= 10 || round % 100 == 0)
                Console.WriteLine($"Round {round}: {a} vs {b} → Player {(winner == p1 ? 1 : 2)} takes {pile.Count} cards");
            foreach (var c in pile.OrderBy(_ => Random.Shared.Next())) winner.Enqueue(c);
            pile.Clear();
            break;
        }
        Console.WriteLine($"Round {round}: {a} vs {b} → WAR!");
        for (int i = 0; i < 3 && p1.Count > 1 && p2.Count > 1; i++)
        {
            pile.Add(p1.Dequeue());
            pile.Add(p2.Dequeue());
        }
    } while (true);
}
Console.WriteLine($"After {round} rounds: Player 1 has {p1.Count}, Player 2 has {p2.Count}");
Console.WriteLine(p1.Count == p2.Count ? "It's a draw!" : $"Player {(p1.Count > p2.Count ? 1 : 2)} wins!");

public enum Suit { Clubs, Diamonds, Hearts, Spades }
public enum Rank { Two = 2, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace }

public record Card(Rank Rank, Suit Suit)
{
    public override string ToString()
    {
        string r = (int)Rank <= 10 ? ((int)Rank).ToString() : Rank.ToString()[..1];
        string s = Suit switch { Suit.Clubs => "♣", Suit.Diamonds => "♦", Suit.Hearts => "♥", _ => "♠" };
        return r + s;
    }
}
