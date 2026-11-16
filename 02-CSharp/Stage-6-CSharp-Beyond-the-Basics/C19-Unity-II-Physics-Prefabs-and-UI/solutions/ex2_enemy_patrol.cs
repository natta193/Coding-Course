using UnityEngine;

public class PatrolEnemy : MonoBehaviour
{
    public Transform pointA, pointB;
    public float speed = 2f;
    private Transform target;
    private SpriteRenderer sr;

    void Start()
    {
        target = pointB;
        sr = GetComponent<SpriteRenderer>();
    }

    void Update()
    {
        transform.position = Vector3.MoveTowards(transform.position, target.position, speed * Time.deltaTime);
        if (Vector3.Distance(transform.position, target.position) < 0.05f)
            target = target == pointA ? pointB : pointA;
        sr.flipX = target.position.x < transform.position.x;
    }

    void OnCollisionEnter2D(Collision2D c)
    {
        if (!c.gameObject.CompareTag("Player")) return;
        // the normal points from the player into this enemy; pointing down = player landed on top
        if (c.GetContact(0).normal.y < -0.5f)
        {
            c.rigidbody.linearVelocity = new Vector2(c.rigidbody.linearVelocity.x, 8f);   // bounce
            Destroy(gameObject);
        }
        else
        {
            GameManager.Instance.GameOver();
        }
    }
}
