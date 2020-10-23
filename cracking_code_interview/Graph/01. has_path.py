import queue
from package.Graph import Graph

def has_path(a: Graph.Node, b: Graph.Node):
  return has_path_helper(a, b) or has_path_helper(b, a)

def has_path_helper(root: Graph.Node, target: Graph.Node):
  q = queue.Queue()
  q.put(root)
  marked = set([root])
  while not q.empty():
    node = q.get()
    if node == target:
      return True
    for n in node.children:
      if n in marked:
        continue
      q.put(n)
      marked.add(n)
  return False

g = Graph([
  [0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0]
])
print(has_path(g.nodes[0], g.nodes[3]))
print(has_path(g.nodes[0], g.nodes[6]))