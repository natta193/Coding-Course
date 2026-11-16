using UnityEngine;
using UnityEngine.InputSystem;
public class PlatformerPlayer : MonoBehaviour
{
    public float speed = 6f, jumpForce = 12f;
    private Rigidbody2D rb;
    private bool grounded;
    void Awake() => rb = GetComponent<Rigidbody2D>();

    void Update()
    {
        var kb = Keyboard.current;
        float x = kb.dKey.isPressed ? 1 : kb.aKey.isPressed ? -1 : 0;
        var v = rb.linearVelocity;
        v.x = x * speed;
        if (kb.spaceKey.wasPressedThisFrame && grounded)
            v.y = jumpForce;
        rb.linearVelocity = v;
    }
}   // ground check: next slide
