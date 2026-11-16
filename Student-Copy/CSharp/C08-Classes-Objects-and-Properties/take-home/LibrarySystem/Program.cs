// TAKE-HOME PROJECT: Library System
// After lesson C08 (Classes, Objects and Properties) - about 1–2 hours, in chunks over the next few days.
//
// Model a school library with classes, properties and encapsulation.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. Book class: Title, Author, Isbn (read-only), and IsOnLoan with a private setter
//   [ ] 2. Member class: Name, a read-only list of borrowed books (max 3)
//   [ ] 3. Library class with private lists of books and members; methods AddBook, Join,
//          Lend(isbn, memberName), Return(isbn) – each returns bool and prints why it failed
//   [ ] 4. Search(string text) finds books by partial title or author
//   [ ] 5. A menu loop in top-level code that only talks to the Library – never to the lists
//          directly
//
// Stretch: Add due dates (DateTime.Today.AddDays(14)) and a "who's overdue?" report.
//
// Bring it to the next session - working or stuck, both are fine.

var library = new Library();

public class Book
{
}

public class Member
{
}

public class Library
{
}
