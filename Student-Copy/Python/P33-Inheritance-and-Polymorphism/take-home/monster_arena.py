# TAKE-HOME PROJECT: Monster Battle Arena
# After lesson P33 (Inheritance and Polymorphism) - about 1–2 hours, in chunks over the next few days.
#
# A tournament of monsters built with inheritance and polymorphism.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. A base Monster class: name, hp, attack, take_damage(), is_alive(), act(opponent)
#          (a normal attack) and __str__
#   [ ] 2. At least 4 subclasses that override act() with a special move: e.g. FireDragon
#          (burn damage over time), Slime (splits/heals), Vampire (steals hp), Turtle (blocks
#          every other hit by overriding take_damage)
#   [ ] 3. Use super() in every subclass constructor
#   [ ] 4. battle(a, b) runs a fight turn by turn and returns the winner
#   [ ] 5. A round-robin tournament: every monster fights every other once; print a league
#          table of wins
#
# Stretch: Add a Trainer class that HAS a team of 3 monsters (composition) and fight
# trainer vs trainer.
#
# Bring it to the next session - working or stuck, both are fine.

import random

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
