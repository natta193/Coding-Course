static int Max(int a, int b) => a > b ? a : b;
static double Max(double a, double b) => a > b ? a : b;
static int Max(int a, int b, int c) => Max(Max(a, b), c);

Console.WriteLine(Max(3, 9));        // int version
Console.WriteLine(Max(2.5, 1.5));    // double version
Console.WriteLine(Max(4, 8, 6));     // 3-parameter version
