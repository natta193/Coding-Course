var rnd = Random.Shared;
var shapes = new List<Shape>();
for (int i = 0; i < 10; i++)
{
    shapes.Add(rnd.Next(3) switch
    {
        0 => new Circle(rnd.Next(1, 6)),
        1 => new Rectangle(rnd.Next(1, 8), rnd.Next(1, 8)),
        _ => new Triangle(3, 4, 5),
    });
}
shapes.Sort();
shapes.ForEach(Console.WriteLine);
Console.WriteLine($"Total area: {shapes.Sum(s => s.Area()):F2}");

public abstract class Shape : IComparable<Shape>
{
    public abstract double Area();
    public int CompareTo(Shape? other) => other is null ? 1 : Area().CompareTo(other.Area());
    public override string ToString() => $"{GetType().Name,-10} area {Area(),7:F2}";
}

public class Circle : Shape
{
    private readonly double r;
    public Circle(double r) => this.r = r;
    public override double Area() => Math.PI * r * r;
}

public class Rectangle : Shape
{
    private readonly double w, h;
    public Rectangle(double w, double h) { this.w = w; this.h = h; }
    public override double Area() => w * h;
}

public class Triangle : Shape
{
    private readonly double a, b, c;
    public Triangle(double a, double b, double c) { this.a = a; this.b = b; this.c = c; }
    public override double Area()
    {
        double s = (a + b + c) / 2;
        return Math.Sqrt(s * (s - a) * (s - b) * (s - c));
    }
}
