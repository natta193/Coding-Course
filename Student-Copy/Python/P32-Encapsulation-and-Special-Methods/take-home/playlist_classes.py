# TAKE-HOME PROJECT: Playlist Classes
# After lesson P32 (Encapsulation and Special Methods) - about 1–2 hours, in chunks over the next few days.
#
# Rebuild your P09 playlist with proper classes that behave like built-in types using
# special (dunder) methods.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Song class: title, artist, seconds. __str__ shows "Title – Artist (3:25)"; __eq__
#          compares title + artist
#   [ ] 2. length is a @property that formats seconds as m:ss
#   [ ] 3. Playlist class holding a list of songs: add(), remove(), shuffle()
#   [ ] 4. Special methods: __len__ (number of songs), __str__ (numbered list + total time),
#          __contains__ (so song in playlist works), __add__ (two playlists → a new combined
#          one)
#   [ ] 5. Test every method with a few lines of code at the bottom
#
# Stretch: Make Playlist iterable (__iter__) and sortable by length with __lt__ on Song.
#
# Bring it to the next session - working or stuck, both are fine.

class Song:
    def __init__(self, title, artist, seconds):
        self.title = title
