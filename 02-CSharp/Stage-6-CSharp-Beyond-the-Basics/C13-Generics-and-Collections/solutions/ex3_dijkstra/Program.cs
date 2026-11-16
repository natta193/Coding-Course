var roads = new Dictionary<string, List<(string To, int Km)>>();

void Road(string a, string b, int km)
{
    if (!roads.ContainsKey(a)) roads[a] = new();
    if (!roads.ContainsKey(b)) roads[b] = new();
    roads[a].Add((b, km));
    roads[b].Add((a, km));
}

Road("Cambridge", "Ely", 26); Road("Cambridge", "Newmarket", 21);
Road("Ely", "King's Lynn", 47); Road("Newmarket", "Bury", 23);
Road("Bury", "Thetford", 19); Road("Ely", "Thetford", 35);
Road("Thetford", "Norwich", 47); Road("King's Lynn", "Norwich", 70);

(int, List<string>) Dijkstra(string start, string goal)
{
    var dist = roads.Keys.ToDictionary(k => k, _ => int.MaxValue);
    var prev = new Dictionary<string, string>();
    var pq = new PriorityQueue<string, int>();
    dist[start] = 0;
    pq.Enqueue(start, 0);
    while (pq.TryDequeue(out string? town, out int d))
    {
        if (d > dist[town]) continue;
        if (town == goal) break;
        foreach (var (to, km) in roads[town])
        {
            int nd = d + km;
            if (nd < dist[to])
            {
                dist[to] = nd;
                prev[to] = town;
                pq.Enqueue(to, nd);
            }
        }
    }
    var path = new List<string> { goal };
    while (path[0] != start) path.Insert(0, prev[path[0]]);
    return (dist[goal], path);
}

var (km, route) = Dijkstra("Cambridge", "Norwich");
Console.WriteLine($"{km} km: {string.Join(" → ", route)}");
