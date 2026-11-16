SIZE = 5
queue = [None] * SIZE
front = 0
rear = -1
count = 0

def enqueue(item):
    global rear, count
    if count == SIZE:
        print("Queue full!")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = item
    count += 1

def dequeue():
    global front, count
    if count == 0:
        print("Queue empty!")
        return None
    item = queue[front]
    queue[front] = None
    front = (front + 1) % SIZE
    count -= 1
    return item

for job in ["essay.docx", "photo.jpg", "map.pdf"]:
    enqueue(job)
print("Printing", dequeue())
for job in ["a", "b", "c", "d"]:
    enqueue(job)               # the last one won't fit
print(queue, "front =", front, "rear =", rear)
while count:
    print("Printing", dequeue())
