var s = new MyStack<int>();
for (int i = 0; i < 10; i++) s.Push(i * i);
Console.WriteLine($"{s.Pop()} {s.Peek()} {s.Count}");

static bool Balanced(string text)
{
    var st = new MyStack<char>();
    foreach (char ch in text)
    {
        if ("([{".Contains(ch)) st.Push(ch);
        else if (")]}".Contains(ch))
        {
            if (st.IsEmpty) return false;
            char open = st.Pop();
            if ("([{".IndexOf(open) != ")]}".IndexOf(ch)) return false;
        }
    }
    return st.IsEmpty;
}
Console.WriteLine($"{Balanced("a(b[c]{d})")} {Balanced("(]")}");

public class MyStack<T>
{
    private T[] items = new T[4];
    private int count;

    public int Count => count;
    public bool IsEmpty => count == 0;

    public void Push(T item)
    {
        if (count == items.Length) Array.Resize(ref items, items.Length * 2);
        items[count++] = item;
    }

    public T Pop()
    {
        if (IsEmpty) throw new InvalidOperationException("Stack is empty");
        T item = items[--count];
        items[count] = default!;
        return item;
    }

    public T Peek() => IsEmpty ? throw new InvalidOperationException("Stack is empty") : items[count - 1];
}
