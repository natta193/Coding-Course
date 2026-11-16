using System;
using UnityEngine;

public class Health : MonoBehaviour, IDamageable
{
    [SerializeField] private int maxHealth = 3;
    public int Current { get; private set; }

    public event Action<int> OnHealthChanged;
    public event Action OnDied;
    void Awake() => Current = maxHealth;

    public void TakeDamage(int amount)
    {
        Current = Mathf.Max(0, Current - amount);
        OnHealthChanged?.Invoke(Current);
        if (Current == 0) OnDied?.Invoke();
    }
}
