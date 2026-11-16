try
{
    string text = File.ReadAllText("save.txt");
}
catch (IOException ex) when (ex is FileNotFoundException)
{
    Console.WriteLine("No save yet – starting fresh");
}
catch (Exception ex)
{
    Console.WriteLine($"Logging: {ex.Message}");
    throw;    // rethrow, keeping the original stack trace
}
