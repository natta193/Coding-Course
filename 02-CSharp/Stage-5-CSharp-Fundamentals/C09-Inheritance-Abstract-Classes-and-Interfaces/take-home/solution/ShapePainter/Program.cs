var canvas = new Canvas(40, 16);
var shapes = new List<Shape>
{
    new Rect(2, 2, 10, 5, '#'),
    new Circle(25, 8, 5, 'o'),
    new Triangle(10, 9, 6, '^'),
    new Rect(33, 1, 5, 3, '='),
    new Circle(6, 12, 2, '@'),
};
foreach (var s in shapes) s.Draw(canvas);
canvas.Show();
foreach (var s in shapes.OfType<IMovable>()) s.Move(1, 1);
canvas.Clear();
foreach (var s in shapes) s.Draw(canvas);
canvas.Show();
Console.WriteLine($"Total area: {shapes.Sum(s => s.Area()):F1}");

public interface IMovable { void Move(int dx, int dy); }

public class Canvas
{
    private readonly char[,] cells;
    public int W { get; }
    public int H { get; }
    public Canvas(int w, int h) { W = w; H = h; cells = new char[h, w]; Clear(); }
    public void Clear() { for (int y = 0; y < H; y++) for (int x = 0; x < W; x++) cells[y, x] = '.'; }
    public void Plot(int x, int y, char ch) { if (x >= 0 && x < W && y >= 0 && y < H) cells[y, x] = ch; }
    public void Show()
    {
        for (int y = 0; y < H; y++)
        {
            for (int x = 0; x < W; x++) Console.Write(cells[y, x]);
            Console.WriteLine();
        }
        Console.WriteLine();
    }
}

public abstract class Shape : IMovable
{
    public int X { get; protected set; }
    public int Y { get; protected set; }
    public char Fill { get; }
    protected Shape(int x, int y, char fill) { X = x; Y = y; Fill = fill; }
    public abstract void Draw(Canvas c);
    public abstract double Area();
    public void Move(int dx, int dy) { X += dx; Y += dy; }
}

public class Rect : Shape
{
    private readonly int w, h;
    public Rect(int x, int y, int w, int h, char fill) : base(x, y, fill) { this.w = w; this.h = h; }
    public override void Draw(Canvas c) { for (int dy = 0; dy < h; dy++) for (int dx = 0; dx < w; dx++) c.Plot(X + dx, Y + dy, Fill); }
    public override double Area() => w * h;
}

public class Circle : Shape
{
    private readonly int r;
    public Circle(int x, int y, int r, char fill) : base(x, y, fill) => this.r = r;
    public override void Draw(Canvas c)
    {
        for (int dy = -r; dy <= r; dy++)
            for (int dx = -2 * r; dx <= 2 * r; dx++)        // x doubled: text cells are tall
                if ((dx / 2.0) * (dx / 2.0) + dy * dy <= r * r) c.Plot(X + dx, Y + dy, Fill);
    }
    public override double Area() => Math.PI * r * r;
}

public class Triangle : Shape
{
    private readonly int h;
    public Triangle(int x, int y, int h, char fill) : base(x, y, fill) => this.h = h;
    public override void Draw(Canvas c)
    {
        for (int row = 0; row < h; row++)
            for (int dx = -row; dx <= row; dx++) c.Plot(X + dx, Y + row, Fill);
    }
    public override double Area() => h * h;
}
