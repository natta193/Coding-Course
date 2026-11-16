bool again;
do
{
    int secret = Random.Shared.Next(1, 101);
    int guesses = 0;
    int guess;
    do
    {
        Console.Write("Guess (1-100): ");
        if (!int.TryParse(Console.ReadLine(), out guess))
        {
            Console.WriteLine("Numbers only!");
            continue;
        }
        guesses++;
        if (guess > secret) Console.WriteLine("Too high!");
        else if (guess < secret) Console.WriteLine("Too low!");
    } while (guess != secret);

    Console.WriteLine($"Correct in {guesses} guesses!");
    Console.Write("Play again? (y/n) ");
    again = (Console.ReadLine() ?? "").Trim().ToLower() == "y";
} while (again);
