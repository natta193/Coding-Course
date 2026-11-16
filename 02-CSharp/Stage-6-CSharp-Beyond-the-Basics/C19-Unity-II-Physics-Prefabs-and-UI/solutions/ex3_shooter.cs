using UnityEngine;
using UnityEngine.InputSystem;

public class TopDownShooter : MonoBehaviour
{
    public GameObject bulletPrefab;
    public float bulletSpeed = 12f;
    public float moveSpeed = 5f;

    void Update()
    {
        var kb = Keyboard.current;
        var mouse = Mouse.current;
        if (kb == null || mouse == null) return;

        Vector2 move = new Vector2(
            (kb.dKey.isPressed ? 1 : 0) - (kb.aKey.isPressed ? 1 : 0),
            (kb.wKey.isPressed ? 1 : 0) - (kb.sKey.isPressed ? 1 : 0)).normalized;
        transform.position += (Vector3)(move * moveSpeed * Time.deltaTime);

        Vector3 mouseWorld = Camera.main.ScreenToWorldPoint(mouse.position.ReadValue());
        Vector2 dir = (mouseWorld - transform.position);
        float angle = Mathf.Atan2(dir.y, dir.x) * Mathf.Rad2Deg;
        transform.rotation = Quaternion.Euler(0, 0, angle);

        if (mouse.leftButton.wasPressedThisFrame)
        {
            GameObject b = Instantiate(bulletPrefab, transform.position, transform.rotation);
            b.GetComponent<Rigidbody2D>().linearVelocity = transform.right * bulletSpeed;
            Destroy(b, 3f);
        }
    }
}

// Bullet.cs – on the bullet prefab (trigger collider + Rigidbody2D, gravity 0)
public class Bullet : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Enemy"))
        {
            Destroy(other.gameObject);
            Destroy(gameObject);
            GameManager.Instance.AddScore(10);
        }
    }
}

// Chaser.cs – on the enemy prefab
public class Chaser : MonoBehaviour
{
    public float speed = 2f;
    private Transform player;

    void Start() => player = GameObject.FindWithTag("Player").transform;

    void Update()
    {
        if (player != null)
            transform.position = Vector2.MoveTowards(transform.position, player.position, speed * Time.deltaTime);
    }
}
