Console.WriteLine("Starting...");        // 1. missing semicolon (CS1002)
int score = 10;
if (score > 5)
{
    Console.WriteLine("Big score!");     // 2. console -> Console (CS0103)
}                                        // 3. missing closing brace (CS1513)
Console.WriteLine("Score: " + score);   // 4. typo scor (CS0103)
Console.WriteLine("Done");               // 5. single quotes are for single chars only (CS1012)
