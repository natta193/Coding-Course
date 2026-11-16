// ===== PlayerController2D.cs =====
using System;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.SceneManagement;

[RequireComponent(typeof(Rigidbody2D))]
public class PlayerController2D : MonoBehaviour
{
    [SerializeField] private float speed = 7f;
    [SerializeField] private float jumpForce = 13f;
    [SerializeField] private float coyoteTime = 0.1f;      // can still jump just after leaving a ledge
    [SerializeField] private float jumpBuffer = 0.1f;      // jump pressed just before landing still counts
    [SerializeField] private LayerMask groundLayer;
    [SerializeField] private Transform feet;

    private Rigidbody2D rb;
    private float lastGrounded = -1f, lastJumpPressed = -1f;

    void Awake() => rb = GetComponent<Rigidbody2D>();

    void Update()
    {
        var kb = Keyboard.current;
        if (kb == null) return;
        float x = (kb.dKey.isPressed || kb.rightArrowKey.isPressed ? 1 : 0)
                - (kb.aKey.isPressed || kb.leftArrowKey.isPressed ? 1 : 0);
        rb.linearVelocity = new Vector2(x * speed, rb.linearVelocity.y);
        if (x != 0) transform.localScale = new Vector3(Mathf.Sign(x), 1, 1);

        if (Physics2D.OverlapCircle(feet.position, 0.1f, groundLayer)) lastGrounded = Time.time;
        if (kb.spaceKey.wasPressedThisFrame) lastJumpPressed = Time.time;

        if (Time.time - lastJumpPressed <= jumpBuffer && Time.time - lastGrounded <= coyoteTime)
        {
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpForce);
            lastJumpPressed = lastGrounded = -1f;
        }
        if (kb.spaceKey.wasReleasedThisFrame && rb.linearVelocity.y > 0)   // short hop when released early
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, rb.linearVelocity.y * 0.5f);
    }
}

// ===== Health.cs =====
public interface IDamageable { void TakeDamage(int amount); }

public class Health : MonoBehaviour, IDamageable
{
    [SerializeField] private int maxHealth = 3;
    public int Max => maxHealth;
    public int Current { get; private set; }
    public event Action<int> OnHealthChanged;
    public event Action OnDied;

    void Awake() => Current = maxHealth;

    public void TakeDamage(int amount)
    {
        if (Current == 0) return;
        Current = Mathf.Max(0, Current - amount);
        OnHealthChanged?.Invoke(Current);
        if (Current == 0) OnDied?.Invoke();
    }

    public void Heal(int amount)
    {
        Current = Mathf.Min(maxHealth, Current + amount);
        OnHealthChanged?.Invoke(Current);
    }
}

// ===== GameManager.cs =====
public enum GameState { Playing, Paused, Won, Lost }

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }
    public GameState State { get; private set; } = GameState.Playing;
    public int Score { get; private set; }
    public event Action<int> OnScoreChanged;
    public event Action<GameState> OnStateChanged;

    [SerializeField] private Health playerHealth;

    void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
    }

    void Start() => playerHealth.OnDied += () => SetState(GameState.Lost);

    void Update()
    {
        if (Keyboard.current != null && Keyboard.current.escapeKey.wasPressedThisFrame)
            SetState(State == GameState.Paused ? GameState.Playing : GameState.Paused);
    }

    public void AddScore(int points)
    {
        Score += points;
        OnScoreChanged?.Invoke(Score);
    }

    public void Win() => SetState(GameState.Won);

    public void SetState(GameState s)
    {
        if (State is GameState.Won or GameState.Lost) return;
        State = s;
        Time.timeScale = s == GameState.Playing ? 1f : 0f;
        OnStateChanged?.Invoke(s);
    }

    public void Restart()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
}

// ===== HeartsUI.cs =====
public class HeartsUI : MonoBehaviour
{
    [SerializeField] private Health health;
    [SerializeField] private UnityEngine.UI.Image[] hearts;

    void OnEnable() => health.OnHealthChanged += Refresh;
    void OnDisable() => health.OnHealthChanged -= Refresh;

    void Refresh(int current)
    {
        for (int i = 0; i < hearts.Length; i++)
            hearts[i].enabled = i < current;
    }
}
