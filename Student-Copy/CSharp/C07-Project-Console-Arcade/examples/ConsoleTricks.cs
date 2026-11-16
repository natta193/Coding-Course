Console.Clear();
Console.ForegroundColor = ConsoleColor.Green;
Console.WriteLine("=== ARCADE ===");
Console.ResetColor();

Console.CursorVisible = false;
Console.SetCursorPosition(10, 5);      // column, row
Console.Write("@");

ConsoleKeyInfo key = Console.ReadKey(true);   // one key, no Enter
if (key.Key == ConsoleKey.UpArrow) { /* move up */ }

if (Console.KeyAvailable) { /* a key is waiting – non-blocking */ }
Thread.Sleep(100);                     // pause 100 ms
