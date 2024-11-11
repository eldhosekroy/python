import heapq

def best_fs(graph, start, goal, heuristic):
    pq, visited = [(heuristic[start], start)], set()
    
    while pq:
        _, curr = heapq.heappop(pq)
        print(f"Visiting node: {curr}")

        if curr == goal:
            print(f"Goal {goal} reached!")
            return True

        visited.add(curr)
        
        for neighbor in graph[curr]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))
                visited.add(neighbor)
    
    print(f"Goal {goal} is not reachable.")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
heuristic = {
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'E': 0
}
best_fs(graph, 'A', 'E', heuristic)
