import heapq

def best_fs(graph, start, goal, heur):
    pq, visited = [(heur[start], start)], set()
    
    while pq:
        _, curr = heapq.heappop(pq)
        if curr == goal:
            print(f"Goal {goal} reached!")
            return True
        visited.add(curr)
        for nbr in graph[curr]:
            if nbr not in visited:
                heapq.heappush(pq, (heur[nbr], nbr))
                visited.add(nbr)
    
    print(f"Goal {goal} is not reachable.")
    return False

graph = {
    'A': ['B', 'C', 'E'], 'B': ['A', 'D', 'F'], 'C': ['A', 'D'],
    'D': ['B', 'C', 'H'], 'E': ['A', 'F'], 'F': ['B', 'E', 'G'],
    'G': ['F', 'H'], 'H': ['D', 'G']
}

heuristic = {'A': 7, 'B': 6, 'C': 9, 'D': 3, 'E': 8, 'F': 2, 'G': 4, 'H': 0}

best_fs(graph, 'A', 'H', heuristic)
