List<Shape> shapes = new() { new Circle(1), new Square(3), new Circle(2.5) };
foreach (Shape s in shapes)
    Console.WriteLine(s.Describe());

IDamageable[] targets = { new Barrel(), new Player() };
foreach (var t in targets)
{
    t.TakeDamage(30);
    Console.WriteLine($"{t.GetType().Name}: {t.Health}");
}
