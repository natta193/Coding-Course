using System.Text.Json;

var mgr = new SaveManager<GameState>("saves");
mgr.Save("slot1", new GameState("Ana", 3, 120, new List<string> { "sword", "potion" }));
mgr.Save("slot2", new GameState("Ben", 1, 50, new List<string>()));
File.WriteAllText(Path.Combine("saves", "broken.json"), "{ not valid json");

foreach (string slot in mgr.ListSlots())
{
    var state = mgr.Load(slot);
    Console.WriteLine(state is null ? $"{slot}: (corrupt)" : $"{slot}: {state}");
}
mgr.Delete("broken");

public record GameState(string Hero, int Floor, int Gold, List<string> Inventory)
{
    public override string ToString() => $"{Hero} floor {Floor}, {Gold} gold, items: {string.Join(", ", Inventory)}";
}

public record SaveEnvelope<T>(int Version, DateTime Saved, T Data);

public class SaveManager<T> where T : class
{
    private const int CurrentVersion = 1;
    private readonly string folder;
    private static readonly JsonSerializerOptions Options = new() { WriteIndented = true };

    public SaveManager(string folder)
    {
        this.folder = folder;
        Directory.CreateDirectory(folder);
    }

    private string PathFor(string slot) => Path.Combine(folder, slot + ".json");

    public void Save(string slot, T data)
    {
        var env = new SaveEnvelope<T>(CurrentVersion, DateTime.Now, data);
        File.WriteAllText(PathFor(slot), JsonSerializer.Serialize(env, Options));
    }

    public T? Load(string slot)
    {
        try
        {
            var env = JsonSerializer.Deserialize<SaveEnvelope<T>>(File.ReadAllText(PathFor(slot)));
            if (env is null || env.Version > CurrentVersion) return null;
            return env.Data;
        }
        catch (Exception ex) when (ex is JsonException or IOException)
        {
            return null;
        }
    }

    public IEnumerable<string> ListSlots() =>
        Directory.GetFiles(folder, "*.json").Select(f => Path.GetFileNameWithoutExtension(f)).OrderBy(s => s);

    public void Delete(string slot) => File.Delete(PathFor(slot));
}
