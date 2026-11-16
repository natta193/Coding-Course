def push(stack, item):
    stack.append(item)

def pop(stack):
    if not stack:
        print("Stack underflow!")
        return None
    return stack.pop()

def peek(stack):
    return stack[-1] if stack else None

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if not queue:
        print("Queue empty!")
        return None
    return queue.pop(0)

s = []
push(s, 1); push(s, 2)
print(pop(s), pop(s), pop(s))
q = []
enqueue(q, "a"); enqueue(q, "b")
print(dequeue(q), dequeue(q))
