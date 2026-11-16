# TAKE-HOME PROJECT: Generative Art Gallery
# After lesson P19 (Turtle Graphics) - about 1–2 hours, in chunks over the next few days.
#
# Make a gallery of 3 artworks that are different every time you run the program, using
# turtle, functions and random.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Write a move_to(x, y) helper and at least 3 shape functions with parameters (size,
#          colour…)
#   [ ] 2. Artwork 1: a night sky – random stars of random sizes and a moon
#   [ ] 3. Artwork 2: a spirograph – a loop of circles with a turn between each, colours
#          cycling with %
#   [ ] 4. Artwork 3: your own design (a city skyline, a forest, abstract art…)
#   [ ] 5. A menu (turtle.textinput) to choose which artwork to draw; screen.clear() between
#          them
#
# Stretch: Press "s" to save the drawing: turtle.getcanvas().postscript(file="art.eps").
#
# Bring it to the next session - working or stuck, both are fine.

import random
import turtle

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
