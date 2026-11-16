"""
EXAMPLE CAPSTONE PLAN: Revision Buddy
Author: Example

== ANALYSIS ==
Problem: I forget revision topics; flashcards on paper get lost.
Requirements:
1. The user can create decks of flashcards for different subjects.
2. The user can revise a deck; wrong cards come back sooner (spaced repetition).
3. Decks are saved in JSON and load automatically.
4. The user can see stats: cards due today, accuracy per deck.
5. Invalid input never crashes the program.

== DESIGN ==
Classes: Card(question, answer, box, due_date), Deck(name, cards), App(menu loop)
Files: decks.json
Milestones: M1 Card/Deck classes + JSON save/load; M2 revise mode; M3 Leitner boxes + due dates;
M4 stats; M5 validation + tests

== TEST PLAN ==
| 1 | Add card        | "2+2" / "4"     | normal    | card saved          | ok | Y |
| 2 | Empty question  | ""              | erroneous | re-asks             | ok | Y |
| 3 | Box at max (5)  | correct answer  | boundary  | stays at box 5      | ok | Y |

== EVALUATION ==
All 5 requirements met. Next: a pygame or web front end, images on cards.
"""
import datetime
import json

INTERVALS = {1: 0, 2: 1, 3: 3, 4: 7, 5: 14}


class Card:
    def __init__(self, question, answer, box=1, due=None):
        self.question, self.answer, self.box = question, answer, box
        self.due = due or datetime.date.today().isoformat()

    def is_due(self):
        return self.due <= datetime.date.today().isoformat()

    def mark(self, correct):
        self.box = min(5, self.box + 1) if correct else 1
        self.due = (datetime.date.today() + datetime.timedelta(days=INTERVALS[self.box])).isoformat()


def save(decks):
    with open("decks.json", "w") as f:
        json.dump({name: [vars(c) for c in cards] for name, cards in decks.items()}, f, indent=2)


def main():
    decks = {"Example": [Card("Capital of France?", "Paris"), Card("2^10?", "1024")]}
    due = [c for c in decks["Example"] if c.is_due()]
    print(f"{len(due)} cards due today")
    save(decks)


if __name__ == "__main__":
    main()
