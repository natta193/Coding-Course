int[] nums = { 5, 12, 8, 3, 19, 7, 14 };

var evens = nums.Where(n => n % 2 == 0);           // filter
var doubled = nums.Select(n => n * 2);             // transform (map)
var sorted = nums.OrderBy(n => n);
var top3 = nums.OrderByDescending(n => n).Take(3);

Console.WriteLine(string.Join(" ", evens));        // 12 8 14
Console.WriteLine(nums.Sum());                     // 68
Console.WriteLine(nums.Average());                 // 9.71...
Console.WriteLine(nums.Any(n => n > 18));          // True
Console.WriteLine(nums.All(n => n > 0));           // True
Console.WriteLine(nums.First(n => n > 10));        // 12
Console.WriteLine(nums.Count(n => n < 10));        // 4
