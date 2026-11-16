var deck = new Deck();
deck.Shuffle();
var p1 = deck.Deal(5);
var p2 = deck.Deal(5);
Console.WriteLine("P1: " + string.Join(" ", p1) + "  high " + p1.MaxBy(c => c.Value));
Console.WriteLine("P2: " + string.Join(" ", p2) + "  high " + p2.MaxBy(c => c.Value));
Console.WriteLine($"{deck.Count} cards left");

public class Card
{
    public static readonly string[] Ranks = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" };
    public string Rank { get; }
    public char Suit { get; }
    public int Value => Array.IndexOf(Ranks, Rank) + 2;

    public Card(string rank, char suit)
    {
        Rank = rank;
        Suit = suit;
    }

    public override string ToString() => $"{Rank}{Suit}";
}

public class Deck
{
    private readonly List<Card> cards = new();
    public int Count => cards.Count;

    public Deck()
    {
        foreach (char s in "♠♥♦♣")
            foreach (string r in Card.Ranks)
                cards.Add(new Card(r, s));
    }

    public void Shuffle()
    {
        for (int i = cards.Count - 1; i > 0; i--)
        {
            int j = Random.Shared.Next(i + 1);
            (cards[i], cards[j]) = (cards[j], cards[i]);
        }
    }

    public List<Card> Deal(int n)
    {
        var hand = cards.Take(n).ToList();
        cards.RemoveRange(0, n);
        return hand;
    }
}
