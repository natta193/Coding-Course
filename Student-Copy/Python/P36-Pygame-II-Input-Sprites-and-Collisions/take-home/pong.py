# TAKE-HOME PROJECT: Pong
# After lesson P36 (Pygame II – Input, Sprites and Collisions) - about 2 hours, in chunks over the next few days.
#
# The original video game: two-player Pong in pygame, built with sprites and game states.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Two paddles (W/S and Up/Down keys) and a ball that bounces off the top and bottom
#   [ ] 2. The ball bounces off paddles; where it hits the paddle changes its angle
#   [ ] 3. A point when the ball goes past a paddle; the ball resets to the centre heading
#          towards the player who lost the point
#   [ ] 4. Menu → playing → game over (first to 7) states, with SPACE to start/restart
#   [ ] 5. Show the score in big digits at the top
#
# Stretch: Add a 1-player mode where the right paddle is an AI that follows the ball (but
# not perfectly!).
#
# Bring it to the next session - working or stuck, both are fine.

import pygame

W, H = 800, 500
