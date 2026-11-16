from collections import deque

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(path + [nxt])
    return None

print(bfs_path(tube, "Old St", "Oxford Circus"))
