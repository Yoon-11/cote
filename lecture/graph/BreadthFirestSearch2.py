from collections import deque

graph = {
    "A": ["B"],
    "B": ["A", "C", "E"],
    "C": ["B", "D"],
    "D": ["C", "E", "F"],
    "E": ["B", "D", "F"],
    "F": ["D", "E"]
}
visited = []

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

    return visited


print(bfs(graph, 'A'))

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

    return visited

