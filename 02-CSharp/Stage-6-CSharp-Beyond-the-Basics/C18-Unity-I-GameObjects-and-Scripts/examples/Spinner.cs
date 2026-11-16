using UnityEngine;

public class Spinner : MonoBehaviour
{
    public float degreesPerSecond = 90f;    // shows in the Inspector!

    void Start()
    {
        Debug.Log($"{name} has started spinning");
    }

    void Update()
    {
        transform.Rotate(0, 0, degreesPerSecond * Time.deltaTime);
    }
}
