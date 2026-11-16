File.WriteAllText("note.txt", "Hello\nWorld");
string all = File.ReadAllText("note.txt");

File.AppendAllText("log.txt", $"{DateTime.Now}: started\n");

string[] lines = File.ReadAllLines("note.txt");
File.WriteAllLines("copy.txt", lines);

if (File.Exists("save.json")) { /* load it */ }
Directory.CreateDirectory("saves");
string path = Path.Combine("saves", "slot1.json");
