from collections import deque

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items


def balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    s = Stack()
    for ch in text:
        if ch in "([{":
            s.push(ch)
        elif ch in ")]}":
            if s.is_empty() or s.pop() != pairs[ch]:
                return False
    return s.is_empty()

print(balanced("(a[b]{c})"), balanced("(]"))
