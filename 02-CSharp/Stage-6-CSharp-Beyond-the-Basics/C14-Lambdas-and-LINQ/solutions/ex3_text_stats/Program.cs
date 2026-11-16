string text = """
    The quick brown fox jumps over the lazy dog. The dog was not amused, and the fox
    ran into the forest. In the forest the fox found another fox, and the two foxes
    played until the sun went down over the quiet forest and the lazy dog slept.
    """;
var stop = new HashSet<string> { "the", "a", "and", "of", "to", "in", "it", "was", "is" };

var words = text
    .Split(new[] { ' ', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries)
    .Select(w => new string(w.Where(char.IsLetter).ToArray()).ToLower())
    .Where(w => w.Length > 0 && !stop.Contains(w))
    .ToList();

var freq = words.GroupBy(w => w)
                .Select(g => (Word: g.Key, Count: g.Count()))
                .OrderByDescending(x => x.Count).ThenBy(x => x.Word)
                .ToList();

freq.Take(10).ToList().ForEach(x => Console.WriteLine($"{x.Word,-10} {new string('█', x.Count)} {x.Count}"));
Console.WriteLine("Used once: " + string.Join(", ", freq.Where(x => x.Count == 1).Select(x => x.Word)));
words.GroupBy(w => w[0]).OrderBy(g => g.Key).ToList()
     .ForEach(g => Console.WriteLine($"{g.Key}: {g.Average(w => w.Length):F1}"));
