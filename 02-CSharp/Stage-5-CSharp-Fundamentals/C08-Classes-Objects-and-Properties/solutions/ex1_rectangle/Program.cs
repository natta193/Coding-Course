var r = new Rectangle(3, 4);
Console.WriteLine(r);
r.Scale(2);
Console.WriteLine($"{r} area={r.Area} perimeter={r.Perimeter} square={r.IsSquare}");
try
{
    r.Width = -1;
}
catch (ArgumentException ex)
{
    Console.WriteLine("Error: " + ex.Message);
}

public class Rectangle
{
    private double width, height;

    public Rectangle(double width, double height)
    {
        Width = width;
        Height = height;
    }

    public double Width
    {
        get => width;
        set => width = value > 0 ? value : throw new ArgumentException("Width must be positive");
    }

    public double Height
    {
        get => height;
        set => height = value > 0 ? value : throw new ArgumentException("Height must be positive");
    }

    public double Area => Width * Height;
    public double Perimeter => 2 * (Width + Height);
    public bool IsSquare => Width == Height;

    public void Scale(double factor)
    {
        Width *= factor;
        Height *= factor;
    }

    public override string ToString() => $"Rectangle {Width} x {Height}";
}
