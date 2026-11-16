# TAKE-HOME PROJECT: Screensaver
# After lesson P35 (Pygame I – The Game Loop) - about 1–2 hours, in chunks over the next few days.
#
# Make a mesmerising pygame screensaver. Pick at least two effects and switch between them
# with the number keys.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Effect 1: a logo/rectangle bouncing around the edges, changing colour every time
#          it hits a wall (the classic DVD screensaver – does it ever hit a corner exactly?)
#   [ ] 2. Effect 2: fireworks – rockets fly up, burst into 40 particles with gravity that
#          fade out
#   [ ] 3. Effect 3 (your idea): rain, snow, a starfield, Matrix-style falling letters…
#   [ ] 4. Use classes for the moving things (e.g. Particle with update() and draw())
#   [ ] 5. Escape quits; keys 1–3 switch effect
#
# Stretch: Make it fullscreen (pygame.FULLSCREEN) and quit when the mouse moves, like a
# real screensaver.
#
# Bring it to the next session - working or stuck, both are fine.

import random
import pygame

W, H = 800, 600
