var pets = new List<string> { "cat", "dog" };
pets.Add("fish");               // append
pets.Insert(0, "rabbit");
pets.Remove("cat");
pets.RemoveAt(0);
Console.WriteLine(pets.Count);            // 2
Console.WriteLine(pets.Contains("dog"));  // True – like `in`

var nums = new List<int> { 5, 2, 9 };
nums.Sort();
nums.Reverse();
Console.WriteLine(string.Join(" ", nums)); // 9 5 2
