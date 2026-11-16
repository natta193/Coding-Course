using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerMover : MonoBehaviour
{
    public float speed = 5f;

    void Update()
    {
        var kb = Keyboard.current;
        if (kb == null) return;
        float x = (kb.dKey.isPressed ? 1 : 0)
                - (kb.aKey.isPressed ? 1 : 0);
        float y = (kb.wKey.isPressed ? 1 : 0)
                - (kb.sKey.isPressed ? 1 : 0);
        Vector3 move = new Vector3(x, y, 0).normalized;
        transform.position += move * speed * Time.deltaTime;
    }
}
