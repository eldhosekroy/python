from collections import deque
graph = {
 1: [2, 3],
 2: [4, 5],
 3: [6],
 4: [],
 5: [],
 6: []
}
def bfs(graph, node):
    q = deque([node])
    visited = set([node])
    while q:
        curr = q.popleft()
        print(curr, end = "")
        for i in graph[curr]:
            if i not in visited:
                visited.add(i)
                q.append(i)
bfs(graph, 1)

