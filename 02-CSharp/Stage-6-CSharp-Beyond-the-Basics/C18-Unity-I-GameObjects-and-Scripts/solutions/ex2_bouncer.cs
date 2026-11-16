using UnityEngine;

public class Bouncer : MonoBehaviour
{
    public Vector2 velocity = new Vector2(3f, 2f);
    private SpriteRenderer sr;
    private float halfW, halfH;

    void Start()
    {
        sr = GetComponent<SpriteRenderer>();
        halfH = Camera.main.orthographicSize;
        halfW = halfH * Camera.main.aspect;
    }

    void Update()
    {
        Vector3 p = transform.position + (Vector3)(velocity * Time.deltaTime);
        Vector3 size = sr.bounds.extents;
        bool bounced = false;
        if (p.x + size.x > halfW || p.x - size.x < -halfW) { velocity.x = -velocity.x; bounced = true; }
        if (p.y + size.y > halfH || p.y - size.y < -halfH) { velocity.y = -velocity.y; bounced = true; }
        if (bounced) sr.color = Random.ColorHSV(0f, 1f, 0.6f, 1f, 0.8f, 1f);
        else transform.position = p;
    }
}
