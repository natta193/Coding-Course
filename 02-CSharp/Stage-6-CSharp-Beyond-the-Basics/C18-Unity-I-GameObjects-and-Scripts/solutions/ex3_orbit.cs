using UnityEngine;

public class Orbit : MonoBehaviour
{
    public Transform centre;
    public float radius = 3f;
    public float period = 5f;
    public float startAngle = 0f;

    void Update()
    {
        if (centre == null) return;
        float angle = startAngle + 2f * Mathf.PI * Time.time / period;
        Vector3 offset = new Vector3(Mathf.Cos(angle), Mathf.Sin(angle), 0f) * radius;
        transform.position = centre.position + offset;
    }
}
