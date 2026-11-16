using System.Text;

var sb = new StringBuilder();
for (int i = 1; i <= 5; i++)
{
    sb.Append(i);
    sb.Append(", ");
}
sb.Length -= 2;                 // remove last ", "
sb.Insert(0, "Numbers: ");
sb.AppendLine("!");
Console.WriteLine(sb.ToString());   // Numbers: 1, 2, 3, 4, 5!
