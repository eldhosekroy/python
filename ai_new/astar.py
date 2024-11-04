from queue import PriorityQueue

graph = {
    '1': [('2', 1), ('3', 4)],
    '2': [('4', 2)],
    '3': [],
    '4': [('5', 1)],
    '5': []
}

heuristic = {
    '1': 7,
    '2': 6,
    '3': 2,
    '4': 1,
    '5': 0
}

def a_star(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0 + heuristic[start], 0, start))  # (f, g, node)
    visited = set()
    came_from = {start: None}

    while not pq.empty():
        f, g, curr = pq.get()
        print(curr, end=" ")

        if curr == goal:
            print("\nGoal reached!")
            print(came_from)
            return reconstruct_path(came_from, start, goal)

        visited.add(curr)

        for neighbor, cost in graph[curr]:
            if neighbor not in visited:
                new_g = g + cost  # Total cost from start to the neighbor
                new_f = new_g + heuristic[neighbor]  # f = g + h
                pq.put((new_f, new_g, neighbor))
                came_from[neighbor] = curr  # Track the path

    print("No path found")
    return None

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

path = a_star(graph, '1', '5')
print("Path:", path)

