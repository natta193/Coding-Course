from collections import deque

queue = deque()
queue.append("Ana")      # enqueue
queue.append("Ben")
queue.append("Cai")
print(queue.popleft())   # dequeue -> Ana
print(queue.popleft())   # dequeue -> Ben
print(queue)             # deque(['Cai'])
