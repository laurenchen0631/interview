class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node:
            return None

        clones: dict[int, Node] = {node.val: Node(node.val)}
        stack = [node]
        visited = [node.val]
        while stack:
            node = stack.pop()
            clone = clones[node.val]
            for neighbor in node.neighbors:
                v = neighbor.val
                if v not in clones:
                    clones[v] = Node(v)
                clone.neighbors.append(clones[v])
                if v not in visited:
                    visited.append(v)
                    stack.append(neighbor)
        return clones[1]

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.neighbors = [b, d]
b.neighbors = [a, c]
c.neighbors = [b, d]
d.neighbors = [a, c]

s = Solution()
print(s.cloneGraph(a).val)
print(s.cloneGraph(None))
