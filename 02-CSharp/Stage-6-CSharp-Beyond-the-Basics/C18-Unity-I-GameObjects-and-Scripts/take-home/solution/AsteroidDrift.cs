// ===== ShipControls.cs =====
using UnityEngine;
using UnityEngine.InputSystem;

public class ShipControls : MonoBehaviour
{
    public float turnSpeed = 180f;
    public float thrust = 6f;
    public float drag = 0.98f;
    private Vector3 velocity;

    void Update()
    {
        var kb = Keyboard.current;
        if (kb == null) return;
        float turn = (kb.aKey.isPressed ? 1 : 0) - (kb.dKey.isPressed ? 1 : 0);
        transform.Rotate(0, 0, turn * turnSpeed * Time.deltaTime);
        if (kb.wKey.isPressed) velocity += transform.up * thrust * Time.deltaTime;
        velocity *= Mathf.Pow(drag, Time.deltaTime * 60f);
        transform.position += velocity * Time.deltaTime;
    }
}

// ===== ScreenWrap.cs (own file) =====
public class ScreenWrap : MonoBehaviour
{
    void LateUpdate()
    {
        float h = Camera.main.orthographicSize, w = h * Camera.main.aspect;
        Vector3 p = transform.position;
        if (p.x > w) p.x = -w; else if (p.x < -w) p.x = w;
        if (p.y > h) p.y = -h; else if (p.y < -h) p.y = h;
        transform.position = p;
    }
}

// ===== Drifter.cs (own file) – on the asteroid prefab =====
public class Drifter : MonoBehaviour
{
    public Vector3 velocity;
    public float spin;
    void Update()
    {
        transform.position += velocity * Time.deltaTime;
        transform.Rotate(0, 0, spin * Time.deltaTime);
    }
}

// ===== AsteroidSpawner.cs (own file) =====
public class AsteroidSpawner : MonoBehaviour
{
    public Drifter asteroidPrefab;
    public int count = 8;

    void Start()
    {
        float h = Camera.main.orthographicSize, w = h * Camera.main.aspect;
        for (int i = 0; i < count; i++)
        {
            Vector3 pos = new Vector3(Random.Range(-w, w), Random.Range(-h, h), 0);
            if (pos.magnitude < 2f) pos = pos.normalized * 3f;      // don't spawn on the ship
            Drifter a = Instantiate(asteroidPrefab, pos, Quaternion.identity);
            a.velocity = Random.insideUnitCircle.normalized * Random.Range(0.5f, 2f);
            a.spin = Random.Range(-90f, 90f);
            a.transform.localScale *= Random.Range(0.6f, 1.6f);
        }
    }
}
