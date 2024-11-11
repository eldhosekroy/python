from queue import PriorityQueue
graph = {
    '1' : ['2','3'],
    '2' : ['4'],
    '3' : [],
    '4' : ['5'],
    '5' : []
}
hur = {
    '1' : 3,
    '2' : 2,
    '3' : 6,
    '4' : 1,
    '5' : 0
    }
def beefs(graph,start,goal):
    pq = PriorityQueue()
    pq.put((hur[start],start))
    visited = set()
    while not pq.empty():
        heur, curr = pq.get()
        print(curr,end = " ")
        if curr == goal:
            print('goal reached\n')
            return
        visited.add(curr)
        for i in graph[curr]:
            if i not in visited:
                pq.put((hur[i],i))

beefs(graph,'1','5')
