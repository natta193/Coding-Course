import random


class Song:
    def __init__(self, title, artist, seconds):
        self.title = title
        self.artist = artist
        self.seconds = seconds

    @property
    def length(self):
        return f"{self.seconds // 60}:{self.seconds % 60:02d}"

    def __str__(self):
        return f"{self.title} – {self.artist} ({self.length})"

    def __eq__(self, other):
        return (self.title, self.artist) == (other.title, other.artist)

    def __lt__(self, other):
        return self.seconds < other.seconds


class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = list(songs or [])

    def add(self, song):
        if song not in self:
            self.songs.append(song)

    def remove(self, song):
        if song in self:
            self.songs.remove(song)

    def shuffle(self):
        random.shuffle(self.songs)

    def __len__(self):
        return len(self.songs)

    def __contains__(self, song):
        return any(s == song for s in self.songs)

    def __iter__(self):
        return iter(self.songs)

    def __add__(self, other):
        combined = Playlist(f"{self.name} + {other.name}", self.songs)
        for s in other:
            combined.add(s)
        return combined

    def __str__(self):
        total = sum(s.seconds for s in self.songs)
        lines = [f"🎵 {self.name} – {len(self)} songs, {total // 60}m {total % 60}s"]
        lines += [f"  {i}. {s}" for i, s in enumerate(self.songs, 1)]
        return "\n".join(lines)


chill = Playlist("Chill", [Song("Ocean Drive", "Wave Kid", 205), Song("Slow Sun", "Lumen", 241)])
gym = Playlist("Gym", [Song("Run It", "Pulse", 180), Song("Ocean Drive", "Wave Kid", 205)])
print(chill)
both = chill + gym
print(both)
print(len(both), Song("Run It", "Pulse", 0) in both)
for s in sorted(both):
    print(s)
