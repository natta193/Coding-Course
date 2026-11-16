public interface IDamageable
{
    int Health { get; }
    void TakeDamage(int amount);
}

public class Barrel : IDamageable
{
    public int Health { get; private set; } = 20;
    public void TakeDamage(int amount) => Health -= amount;
}

public class Player : IDamageable
{
    public int Health { get; private set; } = 100;
    public void TakeDamage(int amount) => Health -= amount / 2;
}
