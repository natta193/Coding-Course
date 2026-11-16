int[] scores = new int[5];              // 5 zeros
string[] names = { "Ana", "Ben", "Cai" };

scores[0] = 92;
Console.WriteLine(names[1]);            // Ben
Console.WriteLine(names.Length);        // 3
Console.WriteLine(names[^1]);           // Cai (last – like [-1])

Array.Sort(names);
Console.WriteLine(string.Join(", ", names));

names[3] = "Dev";   // IndexOutOfRangeException!
