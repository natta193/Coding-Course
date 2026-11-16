public class Animal
{
    public string Name { get; }
    public Animal(string name) => Name = name;

    public virtual string Speak() => "...";
    public string Intro() => $"I'm {Name} and I say {Speak()}";
}

public class Dog : Animal
{
    public Dog(string name) : base(name) { }
    public override string Speak() => "Woof";
}

public class Cat : Animal
{
    public Cat(string name) : base(name) { }
    public override string Speak() => "Meow";
}
