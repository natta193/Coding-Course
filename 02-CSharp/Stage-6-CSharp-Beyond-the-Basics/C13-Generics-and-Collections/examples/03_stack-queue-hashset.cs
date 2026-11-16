var undo = new Stack<string>();
undo.Push("typed A"); undo.Push("typed B");
Console.WriteLine(undo.Pop());          // typed B (LIFO)

var queue = new Queue<string>();
queue.Enqueue("Ana"); queue.Enqueue("Ben");
Console.WriteLine(queue.Dequeue());     // Ana (FIFO)

var seen = new HashSet<string> { "cat" };
Console.WriteLine(seen.Add("dog"));     // True
Console.WriteLine(seen.Add("cat"));     // False – already there

var tasks = new PriorityQueue<string, int>();
tasks.Enqueue("homework", 2); tasks.Enqueue("fire!", 0);
Console.WriteLine(tasks.Dequeue());     // fire! (lowest priority number first)
