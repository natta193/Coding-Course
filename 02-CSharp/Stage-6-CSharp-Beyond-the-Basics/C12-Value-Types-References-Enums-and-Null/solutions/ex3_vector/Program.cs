var pos = new Vector2(0, 10);
var vel = new Vector2(2, 3);
var gravity = new Vector2(0, -1);
for (int t = 0; t < 10; t++)
{
    pos += vel;
    vel += gravity;
    Console.WriteLine($"t={t + 1}: pos {pos}, speed {vel.Length:F2}");
}
Console.WriteLine(new Vector2(3, 4).Normalized());
Console.WriteLine(new Vector2(1, 1) == new Vector2(1, 1));

public readonly struct Vector2
{
    public double X { get; }
    public double Y { get; }
    public Vector2(double x, double y) { X = x; Y = y; }

    public double Length => Math.Sqrt(X * X + Y * Y);
    public Vector2 Normalized() => Length == 0 ? this : this * (1 / Length);

    public static Vector2 operator +(Vector2 a, Vector2 b) => new(a.X + b.X, a.Y + b.Y);
    public static Vector2 operator -(Vector2 a, Vector2 b) => new(a.X - b.X, a.Y - b.Y);
    public static Vector2 operator *(Vector2 a, double k) => new(a.X * k, a.Y * k);
    public static bool operator ==(Vector2 a, Vector2 b) => a.X == b.X && a.Y == b.Y;
    public static bool operator !=(Vector2 a, Vector2 b) => !(a == b);
    public override bool Equals(object? o) => o is Vector2 v && v == this;
    public override int GetHashCode() => HashCode.Combine(X, Y);
    public override string ToString() => $"({X:F1}, {Y:F1})";
}
