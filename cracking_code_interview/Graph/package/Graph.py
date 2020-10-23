class Graph:
  class Node:
    def __init__(self, name):
      self.name = name
      self.children = []

    def add_path(self, node):
      self.children.append(node)

    def __repr__(self):
      return str(self.name)

  def __init__(self, matrix):
    n = len(matrix)
    self.nodes: list[Graph.Node] = [Graph.Node(i) for i in range(n)]

    for i in range(n):
      node = self.nodes[i]
      for j in range(n):
        if matrix[i][j] == 0:
          continue
        node.add_path(self.nodes[j])

if __name__ == '__main__':
  g1 = Graph([
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
  ])
  for node in g1.nodes:
    print(node.name, node.children)