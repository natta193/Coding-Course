var fleet = new List<Vehicle> { new Car("Mini", "Cooper"), new Motorbike("Honda", "CB500"), new Lorry("Volvo", "FH16", 40) };
foreach (var v in fleet) Console.WriteLine(v.Describe());

public abstract class Vehicle
{
    public string Make { get; }
    public string Model { get; }
    public abstract int Wheels { get; }
    protected Vehicle(string make, string model) { Make = make; Model = model; }
    public virtual string Describe() => $"{Make} {Model} with {Wheels} wheels";
}

public class Car : Vehicle
{
    public Car(string make, string model) : base(make, model) { }
    public override int Wheels => 4;
}

public class Motorbike : Vehicle
{
    public Motorbike(string make, string model) : base(make, model) { }
    public override int Wheels => 2;
}

public class Lorry : Vehicle
{
    public int Cargo { get; }
    public Lorry(string make, string model, int cargo) : base(make, model) => Cargo = cargo;
    public override int Wheels => 18;
    public override string Describe() => base.Describe() + $", carries {Cargo} tonnes";
}
