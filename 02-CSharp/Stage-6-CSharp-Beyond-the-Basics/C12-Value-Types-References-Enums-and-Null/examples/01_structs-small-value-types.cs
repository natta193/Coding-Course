public struct Point
{
    public int X;
    public int Y;
    public Point(int x, int y) { X = x; Y = y; }
    public override string ToString() => $"({X}, {Y})";
}

var p1 = new Point(1, 2);
var p2 = p1;          // COPY
p2.X = 99;
Console.WriteLine(p1);   // (1, 2) – unchanged!
