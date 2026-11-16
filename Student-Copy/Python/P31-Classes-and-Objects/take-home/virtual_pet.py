# TAKE-HOME PROJECT: Virtual Pet
# After lesson P31 (Classes and Objects) - about 1–2 hours, in chunks over the next few days.
#
# A Tamagotchi-style pet as a class. Time passes between your actions, so you have to keep
# it happy!
#
# Milestones (make each one work before starting the next):
#   [ ] 1. A Pet class with name, hunger, happiness and energy (0–10) and an age in turns
#   [ ] 2. Methods: feed(), play(), sleep(), tick() (one turn passing: hunger up, happiness
#          and energy down) and status()
#   [ ] 3. Keep values between 0 and 10 with max/min
#   [ ] 4. is_alive() – the pet runs away if hunger hits 10 or happiness hits 0
#   [ ] 5. A game loop: show status, choose an action, then tick() – how many turns can you
#          keep it going?
#
# Stretch: Own two pets at once (a list of Pet objects); each action asks which pet.
#
# Bring it to the next session - working or stuck, both are fine.

class Pet:
    def __init__(self, name):
        self.name = name
