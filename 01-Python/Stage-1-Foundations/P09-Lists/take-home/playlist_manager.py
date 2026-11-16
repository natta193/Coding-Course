# TAKE-HOME PROJECT: Playlist Manager
# After lesson P09 (Lists) - about 1–2 hours, in chunks over the next few days.
#
# Build a music playlist manager using lists. (Songs are just text – no actual music!)
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Start with a list of 5 favourite songs. Menu: show, add, remove, move a song up,
#          shuffle, play next, quit
#   [ ] 2. Show: number the songs from 1
#   [ ] 3. Remove by number – check the number is valid first
#   [ ] 4. Move up: swap a song with the one above it (a[i], a[i-1] = a[i-1], a[i])
#   [ ] 5. Play next: pop(0) the first song, print "Now playing…" and add it to a separate
#          "recently played" list
#
# Stretch: Store each song as a small list [title, artist, minutes] and show the
# playlist's total length in minutes.
#
# Bring it to the next session - working or stuck, both are fine.

import random

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
recent = []
