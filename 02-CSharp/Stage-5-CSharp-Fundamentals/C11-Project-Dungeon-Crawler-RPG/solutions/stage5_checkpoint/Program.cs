using System.Text;

// 1
Console.Write("a: ");
int.TryParse(Console.ReadLine(), out int a);
Console.Write("b: ");
int.TryParse(Console.ReadLine(), out int b);
Console.WriteLine($"Sum {a + b}, average {(a + b) / 2.0}");

// 2
static bool IsLeapYear(int y) => (y % 4 == 0 && y % 100 != 0) || y % 400 == 0;
Console.WriteLine($"{IsLeapYear(1900)} {IsLeapYear(2000)} {IsLeapYear(2024)}");

// 3
var names = new List<string> { "Zoe", "Ana", "Max", "Ben", "Kai" };
names.Sort();
Console.WriteLine(string.Join(", ", names));

// 4
var counts = new Dictionary<char, int>();
foreach (char ch in "mississippi") counts[ch] = counts.GetValueOrDefault(ch) + 1;
foreach (var (ch, n) in counts) Console.WriteLine($"{ch}: {n}");

// 5
var c = new Counter();
c.Increment(); c.Increment();
Console.WriteLine(c.Value);

// 6
foreach (Animal an in new List<Animal> { new Dog(), new Cat() }) Console.WriteLine(an.Speak());

// 7
try { int.Parse("oops"); }
catch (Exception ex) { Console.WriteLine(ex.GetType().Name); }

// 8
var sb = new StringBuilder();
for (int i = 1; i <= 20; i++) sb.Append(i).Append(i < 20 ? "-" : "");
Console.WriteLine(sb);

public class Counter
{
    private int count;
    public int Value => count;
    public void Increment() => count++;
    public void Reset() => count = 0;
}

public abstract class Animal { public abstract string Speak(); }
public class Dog : Animal { public override string Speak() => "Woof"; }
public class Cat : Animal { public override string Speak() => "Meow"; }
