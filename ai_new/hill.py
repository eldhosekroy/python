class node:
    def __init__(self, name, values):
        self.name = name
        self.values = values
        self.n = []
def hill(start, goal):
    curr = start
    path = [curr.name]
    while True:
       if curr == goal:
          return path
       if not curr.n:
          break
       next = max(curr.n, key = lambda node: curr.values)
       if next.values <= curr.values:
          break
       curr = next
       path.append(curr.name)
    return None
node_a = node('a', 1)
node_b = node('b', 3)
node_c = node('c', 2)
node_d = node('d', 4)
node_e = node('e', 0)

node_a.n = [node_b, node_c]
node_b.n = [node_d, node_e]
node_c.n = [node_d]
node_d.n = [node_e]
node_e.n = []

result = hill(node_a, node_d)
if result:
    print(result)
else:
    print("no path")

