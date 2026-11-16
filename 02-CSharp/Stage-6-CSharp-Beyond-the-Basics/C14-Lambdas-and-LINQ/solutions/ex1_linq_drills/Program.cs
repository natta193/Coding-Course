var nums = Enumerable.Range(1, 50).ToList();
var words = new List<string> { "apple", "Banana", "cherry", "date", "Elderberry", "fig", "grape" };

Console.WriteLine(string.Join(" ", nums.Where(n => n % 2 == 1).Select(n => n * n)));
Console.WriteLine(nums.Where(n => n % 3 == 0 || n % 5 == 0).Sum());
Console.WriteLine(nums.Any(n => n > 49));
Console.WriteLine(nums.First(n => n * n > 500));
Console.WriteLine(string.Join(" ", nums.Where(n => n >= 10 && n <= 20).OrderByDescending(n => n)));
Console.WriteLine(string.Join(" ", words.Where(w => w.Length > 4).Select(w => w.ToUpper())));
Console.WriteLine(string.Join(" ", words.OrderBy(w => w.Length).ThenBy(w => w.ToLower())));
Console.WriteLine(words.MaxBy(w => w.Length));
Console.WriteLine(words.Count(w => char.IsUpper(w[0])));
Console.WriteLine(words.Sum(w => w.Length));
