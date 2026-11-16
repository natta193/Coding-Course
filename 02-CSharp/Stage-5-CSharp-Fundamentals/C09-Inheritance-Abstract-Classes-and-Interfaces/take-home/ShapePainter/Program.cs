// TAKE-HOME PROJECT: ASCII Shape Painter
// After lesson C09 (Inheritance, Abstract Classes and Interfaces) - about 1–2 hours, in chunks over the next few days.
//
// An abstract Shape class whose subclasses draw themselves onto a text "canvas" –
// polymorphism you can see.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. A Canvas class wrapping a char[,] (e.g. 40×20) with Plot(x, y, ch) (ignore off-
//          canvas points) and Show()
//   [ ] 2. abstract class Shape with X, Y, a fill char, abstract void Draw(Canvas c) and
//          abstract double Area()
//   [ ] 3. Subclasses: Rect, Circle (plot points where (dx²+dy²) ≤ r²), Triangle
//   [ ] 4. An IMovable interface with Move(dx, dy) – implement it on all shapes
//   [ ] 5. Put 5 shapes in a List<Shape>, draw them all, move them, draw again; print the
//          total area
//
// Stretch: Add a Text shape that draws a word, and a "scene file" format you read to
// create shapes.
//
// Bring it to the next session - working or stuck, both are fine.

Console.WriteLine("Shape Painter – create a Canvas and some shapes here");

public class Canvas
{
}

public abstract class Shape
{
}
