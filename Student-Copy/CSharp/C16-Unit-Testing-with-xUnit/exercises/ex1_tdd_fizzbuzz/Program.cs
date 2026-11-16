static string FizzBuzz(int n) => "";   // TODO – after writing tests!

int passed = 0, failed = 0;
void Check(string name, bool ok)
{
    if (ok) passed++; else { failed++; Console.WriteLine($"FAIL: {name}"); }
}

Check("1 -> 1", FizzBuzz(1) == "1");
// add more tests here

Console.WriteLine($"{passed} passed, {failed} failed");
