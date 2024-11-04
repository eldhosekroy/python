from sys import maxsize
from itertools import permutations
v  = 4
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
def tsp():
    vertex = [1, 2, 3]
    minsize = maxsize
    nextp = permutations(vertex)
    for i in nextp: 
        k = s
        pathcost = 0
        for j in i:
            pathcost += graph[k][j]
            k = j
        pathcost += graph[k][s]
        minsize = min(pathcost, minsize)
    return minsize
s = 0
value = tsp()
print("short ", value)

