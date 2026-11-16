// TAKE-HOME PROJECT: Creature Data Analyst
// After lesson C14 (Lambdas and LINQ) - about 1–2 hours, in chunks over the next few days.
//
// Answer questions about a dataset of made-up creatures using nothing but LINQ.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. The starter has a CSV string of 20 creatures: name, type, hp, attack, speed,
//          legendary (true/false)
//   [ ] 2. Parse it into a List<Creature> record with Split and Select
//   [ ] 3. Answer 8 questions, one LINQ query each: strongest attacker; average hp per type;
//          all legendaries sorted by speed; types with more than 3 creatures; the fastest of
//          each type; anyone whose attack > hp; total hp of the top 5 by attack; is there any
//          creature with speed over 100?
//   [ ] 4. Print each answer neatly with the question above it
//   [ ] 5. Invent 2 questions of your own and answer them
//
// Stretch: Write the same queries in "query syntax" (from c in creatures where … select …)
// and compare readability.
//
// Bring it to the next session - working or stuck, both are fine.

const string Data = """
name,type,hp,attack,speed,legendary
Emberfox,fire,45,60,90,false
Tidalon,water,80,55,40,false
""";

public record Creature(string Name, string Type, int Hp, int Attack, int Speed, bool Legendary);
