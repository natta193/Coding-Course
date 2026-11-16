using System.Text.Json;

const string FilePath = "contacts.json";
var opts = new JsonSerializerOptions { WriteIndented = true };

List<Contact> Load() => File.Exists(FilePath)
    ? JsonSerializer.Deserialize<List<Contact>>(File.ReadAllText(FilePath)) ?? new()
    : new();
void Save(List<Contact> cs) => File.WriteAllText(FilePath, JsonSerializer.Serialize(cs, opts));

string Ask(string prompt) { Console.Write(prompt); return (Console.ReadLine() ?? "").Trim(); }

var contacts = Load();
while (true)
{
    string c = Ask("(a)dd (s)earch (d)elete (l)ist (b)irthdays (q)uit: ").ToLower();
    if (c == "q" || c == "") break;
    if (c == "a")
    {
        string name = Ask("Name: ");
        string phone = Ask("Phone: ");
        string email = Ask("Email: ");
        DateOnly.TryParse(Ask("Birthday (yyyy-mm-dd): "), out DateOnly bday);
        contacts.Add(new Contact(name, phone, email, bday));
        Save(contacts);
    }
    else if (c == "s")
    {
        string q = Ask("Search: ").ToLower();
        foreach (var ct in contacts.Where(x => x.Name.ToLower().Contains(q))) Console.WriteLine(ct);
    }
    else if (c == "d")
    {
        string name = Ask("Delete who? ");
        int removed = contacts.RemoveAll(x => x.Name.Equals(name, StringComparison.OrdinalIgnoreCase));
        Console.WriteLine($"Removed {removed}");
        Save(contacts);
    }
    else if (c == "l")
    {
        foreach (var ct in contacts.OrderBy(x => x.Name)) Console.WriteLine($"{ct.Name,-15} {ct.Phone,-14} {ct.Email}");
    }
    else if (c == "b")
    {
        var today = DateOnly.FromDateTime(DateTime.Today);
        foreach (var ct in contacts)
        {
            var next = new DateOnly(today.Year, ct.Birthday.Month, Math.Min(ct.Birthday.Day, 28));
            if (next < today) next = next.AddYears(1);
            int days = next.DayNumber - today.DayNumber;
            if (days <= 30) Console.WriteLine($"{ct.Name}: in {days} days");
        }
    }
}

record Contact(string Name, string Phone, string Email, DateOnly Birthday);
