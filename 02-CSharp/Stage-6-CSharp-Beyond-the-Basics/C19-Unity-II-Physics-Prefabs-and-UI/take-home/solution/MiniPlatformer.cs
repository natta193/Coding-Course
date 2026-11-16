// ===== Respawner.cs – on the player =====
using TMPro;
using UnityEngine;

public class Respawner : MonoBehaviour
{
    public Vector3 respawnPoint;
    private Rigidbody2D rb;

    void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
        respawnPoint = transform.position;
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Hazard"))
        {
            transform.position = respawnPoint;
            rb.linearVelocity = Vector2.zero;
        }
        else if (other.TryGetComponent(out Checkpoint cp))
        {
            respawnPoint = cp.transform.position;
            cp.Activate();
        }
    }
}

// ===== Checkpoint.cs (own file) =====
public class Checkpoint : MonoBehaviour
{
    public Color activeColour = Color.green;
    public void Activate() => GetComponent<SpriteRenderer>().color = activeColour;
}

// ===== LevelManager.cs (own file) =====
public class LevelManager : MonoBehaviour
{
    public static LevelManager Instance { get; private set; }
    public TMP_Text scoreText;
    public TMP_Text finishText;
    private int coins;
    private float startTime;

    void Awake()
    {
        Instance = this;
        startTime = Time.time;
        finishText.gameObject.SetActive(false);
    }

    public void AddCoin()
    {
        coins++;
        scoreText.text = $"Coins: {coins}";
    }

    public void Finish()
    {
        finishText.text = $"Level complete!\n{coins} coins in {Time.time - startTime:F1} seconds";
        finishText.gameObject.SetActive(true);
        Time.timeScale = 0;
    }
}

// ===== Goal.cs (own file) – on the flag (trigger collider) =====
public class Goal : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player")) LevelManager.Instance.Finish();
    }
}

// ===== MovingPlatform.cs (own file) – Kinematic Rigidbody2D =====
public class MovingPlatform : MonoBehaviour
{
    public Transform a, b;
    public float speed = 2f;
    private Rigidbody2D rb;
    private Transform target;

    void Awake() { rb = GetComponent<Rigidbody2D>(); target = b; }

    void FixedUpdate()
    {
        Vector2 next = Vector2.MoveTowards(rb.position, target.position, speed * Time.fixedDeltaTime);
        rb.MovePosition(next);
        if (Vector2.Distance(next, target.position) < 0.05f) target = target == a ? b : a;
    }
}
