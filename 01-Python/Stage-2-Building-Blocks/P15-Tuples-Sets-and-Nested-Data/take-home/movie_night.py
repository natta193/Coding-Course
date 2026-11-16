# TAKE-HOME PROJECT: Movie Night Planner
# After lesson P15 (Tuples, Sets and Nested Data) - about 1–2 hours, in chunks over the next few days.
#
# Help a group of friends choose a film. Each movie is a dictionary inside a list, and
# sets work out what everyone can agree on.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Make a list of at least 8 movies: title, year, age rating (as a number), length in
#          minutes, and a list of genres
#   [ ] 2. Ask how many friends; for each, ask their age and which genres they like (comma-
#          separated) – store each friend's genres as a **set**
#   [ ] 3. Find the genres EVERYONE likes (set intersection) and the youngest friend's age
#   [ ] 4. Shortlist movies suitable for the youngest friend that have at least one shared
#          genre
#   [ ] 5. Print the shortlist sorted by length, and pick a random winner
#
# Stretch: Let each friend vote for one film on the shortlist; count votes with a
# dictionary and announce the winner (random tiebreak).
#
# Bring it to the next session - working or stuck, both are fine.

import random

movies = [
    {"title": "Space Rescue", "year": 2021, "rating": 12, "minutes": 118, "genres": ["sci-fi", "action"]},
]
