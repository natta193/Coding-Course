public abstract class Shape
{
    public abstract double Area();    // no body: must override
    public virtual string Describe() =>
        $"{GetType().Name} with area {Area():F2}";
}

public class Circle : Shape
{
    public double R { get; }
    public Circle(double r) => R = r;
    public override double Area() => Math.PI * R * R;
}

// var s = new Shape();   // compile error: abstract
