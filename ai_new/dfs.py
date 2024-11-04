graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : [],
        }
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end = "")
        visited.add(node)
    for i in graph[node]:
        dfs(visited, graph, i)
visited = set()
dfs(visited, graph, 'A')
