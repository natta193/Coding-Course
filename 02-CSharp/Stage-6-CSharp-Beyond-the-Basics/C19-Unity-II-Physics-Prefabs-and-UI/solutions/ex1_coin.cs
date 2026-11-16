using UnityEngine;
using UnityEngine.InputSystem;

public class CatcherPlayer : MonoBehaviour
{
    public float speed = 8f;
    public float limit = 8f;

    void Update()
    {
        var kb = Keyboard.current;
        if (kb == null) return;
        float x = (kb.rightArrowKey.isPressed || kb.dKey.isPressed ? 1 : 0)
                - (kb.leftArrowKey.isPressed || kb.aKey.isPressed ? 1 : 0);
        Vector3 p = transform.position + Vector3.right * x * speed * Time.deltaTime;
        p.x = Mathf.Clamp(p.x, -limit, limit);
        transform.position = p;
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.TryGetComponent(out Coin coin))
        {
            GameManager.Instance.AddScore(coin.value);
            Destroy(other.gameObject);
        }
        else if (other.CompareTag("Bomb"))
        {
            GameManager.Instance.GameOver();
        }
    }
}

// Put this in its own file Coin.cs (Unity needs one MonoBehaviour per file, named the same)
public class Coin : MonoBehaviour
{
    public int value = 1;
    public float spinSpeed = 180f;

    void Update() => transform.Rotate(0f, spinSpeed * Time.deltaTime, 0f);
}
