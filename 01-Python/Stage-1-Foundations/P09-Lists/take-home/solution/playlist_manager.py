import random

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
recent = []

while True:
    c = input("(s)how (a)dd (r)emove (u)p (x) shuffle (p)lay (q)uit: ").lower().strip()
    if c == "q":
        break
    elif c == "s":
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song}")
        print("Recently played:", recent[-3:])
    elif c == "a":
        playlist.append(input("Song: "))
    elif c == "r":
        n = int(input("Number to remove: "))
        if 1 <= n <= len(playlist):
            print("Removed", playlist.pop(n - 1))
        else:
            print("No song with that number")
    elif c == "u":
        n = int(input("Number to move up: "))
        if 2 <= n <= len(playlist):
            i = n - 1
            playlist[i], playlist[i - 1] = playlist[i - 1], playlist[i]
    elif c == "x":
        random.shuffle(playlist)
        print("Shuffled!")
    elif c == "p":
        if playlist:
            song = playlist.pop(0)
            recent.append(song)
            print("Now playing:", song)
        else:
            print("Playlist empty")
