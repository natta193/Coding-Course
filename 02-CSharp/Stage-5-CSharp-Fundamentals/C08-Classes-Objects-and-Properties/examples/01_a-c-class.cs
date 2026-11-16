public class Dog
{
    private int energy = 10;               // field (private!)

    public string Name { get; }            // read-only property
    public string Breed { get; set; }      // auto-property

    public Dog(string name, string breed)  // constructor
    {
        Name = name;
        Breed = breed;
    }

    public void Bark() => Console.WriteLine($"{Name} says Woof!");

    public void Play(int minutes)
    {
        energy -= minutes / 10;
        Console.WriteLine($"{Name} has {energy} energy");
    }
}
