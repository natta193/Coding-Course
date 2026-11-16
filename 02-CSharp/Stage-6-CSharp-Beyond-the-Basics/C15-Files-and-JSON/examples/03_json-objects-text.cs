using System.Text.Json;

var save = new SaveData("Ana", 7, new List<string> { "sword", "potion" });

var options = new JsonSerializerOptions { WriteIndented = true };
string json = JsonSerializer.Serialize(save, options);
File.WriteAllText("save.json", json);

string text = File.ReadAllText("save.json");
SaveData? loaded = JsonSerializer.Deserialize<SaveData>(text);
Console.WriteLine(loaded?.Items[0]);    // sword

public record SaveData(string Name, int Level, List<string> Items);
