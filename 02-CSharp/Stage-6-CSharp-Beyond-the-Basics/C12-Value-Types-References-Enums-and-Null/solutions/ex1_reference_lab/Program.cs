int i1 = 5; int i2 = i1; i2 = 9;
Console.WriteLine($"int: {i1}");                   // 5 – value copied

var s1 = new PointS { X = 1 }; var s2 = s1; s2.X = 9;
Console.WriteLine($"struct: {s1.X}");              // 1 – struct copied

var c1 = new PointC { X = 1 }; var c2 = c1; c2.X = 9;
Console.WriteLine($"class: {c1.X}");               // 9 – same object!

int[] a1 = { 1, 2 }; int[] a2 = a1; a2[0] = 9;
Console.WriteLine($"array: {a1[0]}");              // 9 – arrays are reference types

var r1 = new PointR(1); var r2 = r1 with { X = 9 };
Console.WriteLine($"record: {r1.X}");              // 1 – 'with' makes a new copy

public struct PointS { public int X; }
public class PointC { public int X; }
public record PointR(int X);
