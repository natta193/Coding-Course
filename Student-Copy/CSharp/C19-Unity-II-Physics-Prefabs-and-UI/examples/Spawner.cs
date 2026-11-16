using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject coinPrefab;     // drag the prefab here
    public float every = 1.5f;
    private float timer;

    void Update()
    {
        timer += Time.deltaTime;
        if (timer >= every)
        {
            timer = 0;
            var pos = new Vector3(Random.Range(-8f, 8f), 6f, 0);
            var coin = Instantiate(coinPrefab, pos,
                                   Quaternion.identity);
            Destroy(coin, 10f);       // clean up after 10 s
        }
    }
}
