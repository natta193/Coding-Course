from collections import deque

back_stack = []
forward_stack = []
recent = deque(maxlen=5)
bookmarks = set()
current = "home"

while True:
    print(f"\n📄 {current}   (back: {len(back_stack)}, forward: {len(forward_stack)})")
    cmd = input("> ").strip().split(maxsplit=1)
    if not cmd:
        continue
    if cmd[0] == "visit" and len(cmd) == 2:
        back_stack.append(current)
        forward_stack.clear()
        current = cmd[1]
        recent.append(current)
    elif cmd[0] == "back":
        if back_stack:
            forward_stack.append(current)
            current = back_stack.pop()
        else:
            print("Nothing to go back to.")
    elif cmd[0] == "forward":
        if forward_stack:
            back_stack.append(current)
            current = forward_stack.pop()
        else:
            print("Nothing to go forward to.")
    elif cmd[0] == "history":
        print("Recently visited:", list(recent))
    elif cmd[0] == "bookmark":
        bookmarks.add(current)
    elif cmd[0] == "bookmarks":
        print(sorted(bookmarks))
    elif cmd[0] == "quit":
        break
    else:
        print("Commands: visit <url>, back, forward, history, bookmark, bookmarks, quit")
