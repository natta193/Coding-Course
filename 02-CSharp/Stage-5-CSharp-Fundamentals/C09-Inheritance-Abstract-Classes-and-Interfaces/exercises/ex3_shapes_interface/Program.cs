Console.WriteLine("Write your code here!");

public abstract class Shape : IComparable<Shape>
{
    public abstract double Area();
    public int CompareTo(Shape? other) => 0; // fix me
}
