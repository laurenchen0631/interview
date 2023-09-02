class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        visited = set()
        while p or q:
            if p:
                if p in visited:
                    return p
                visited.add(p)
                p = p.parent
            if q:
                if q in visited:
                    return q
                visited.add(q)
                q = q.parent
        