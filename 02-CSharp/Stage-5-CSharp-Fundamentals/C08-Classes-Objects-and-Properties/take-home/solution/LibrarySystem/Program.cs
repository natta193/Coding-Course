var library = new Library();
library.AddBook(new Book("The Hobbit", "J. R. R. Tolkien", "111"));
library.AddBook(new Book("Holes", "Louis Sachar", "222"));
library.AddBook(new Book("Wonder", "R. J. Palacio", "333"));
library.Join("Ana");
library.Join("Ben");

while (true)
{
    Console.Write("\n(s)earch (l)end (r)eturn (b)ooks (q)uit: ");
    string c = (Console.ReadLine() ?? "q").Trim().ToLower();
    if (c == "q" || c == "") break;
    if (c == "s") { Console.Write("Search: "); foreach (var b in library.Search(Console.ReadLine() ?? "")) Console.WriteLine("  " + b); }
    else if (c == "b") foreach (var b in library.Search("")) Console.WriteLine("  " + b);
    else if (c == "l")
    {
        Console.Write("ISBN: "); string isbn = Console.ReadLine() ?? "";
        Console.Write("Member: "); string who = Console.ReadLine() ?? "";
        library.Lend(isbn, who);
    }
    else if (c == "r") { Console.Write("ISBN: "); library.Return(Console.ReadLine() ?? ""); }
}

public class Book
{
    public string Title { get; }
    public string Author { get; }
    public string Isbn { get; }
    public bool IsOnLoan { get; private set; }
    public DateTime? Due { get; private set; }

    public Book(string title, string author, string isbn) { Title = title; Author = author; Isbn = isbn; }

    public void Lend() { IsOnLoan = true; Due = DateTime.Today.AddDays(14); }
    public void Return() { IsOnLoan = false; Due = null; }

    public override string ToString() => $"{Title} by {Author} [{Isbn}]" + (IsOnLoan ? $" – on loan until {Due:dd MMM}" : "");
}

public class Member
{
    public const int MaxBooks = 3;
    private readonly List<Book> borrowed = new();
    public string Name { get; }
    public IReadOnlyList<Book> Borrowed => borrowed;

    public Member(string name) => Name = name;
    public bool CanBorrow => borrowed.Count < MaxBooks;
    public void Take(Book b) => borrowed.Add(b);
    public void Give(Book b) => borrowed.Remove(b);
}

public class Library
{
    private readonly List<Book> books = new();
    private readonly List<Member> members = new();

    public void AddBook(Book b) => books.Add(b);
    public void Join(string name) => members.Add(new Member(name));

    public IEnumerable<Book> Search(string text) =>
        books.Where(b => b.Title.Contains(text, StringComparison.OrdinalIgnoreCase)
                      || b.Author.Contains(text, StringComparison.OrdinalIgnoreCase));

    public bool Lend(string isbn, string memberName)
    {
        var book = books.FirstOrDefault(b => b.Isbn == isbn);
        var member = members.FirstOrDefault(m => m.Name.Equals(memberName, StringComparison.OrdinalIgnoreCase));
        if (book is null) { Console.WriteLine("No such book."); return false; }
        if (member is null) { Console.WriteLine("No such member."); return false; }
        if (book.IsOnLoan) { Console.WriteLine("Already on loan."); return false; }
        if (!member.CanBorrow) { Console.WriteLine($"{member.Name} already has {Member.MaxBooks} books."); return false; }
        book.Lend();
        member.Take(book);
        Console.WriteLine($"Lent {book.Title} to {member.Name}.");
        return true;
    }

    public bool Return(string isbn)
    {
        var member = members.FirstOrDefault(m => m.Borrowed.Any(b => b.Isbn == isbn));
        if (member is null) { Console.WriteLine("That book isn't on loan."); return false; }
        var book = member.Borrowed.First(b => b.Isbn == isbn);
        member.Give(book);
        book.Return();
        Console.WriteLine($"{book.Title} returned.");
        return true;
    }
}
