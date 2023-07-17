# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        parents = self.build_reversed_graph(root)
        if p not in parents or q not in parents:
            return None
        visited = set([p, q])
        queue = deque([p, q])
        while q:
            node = queue.popleft()
            if node in parents:
                if parents[node] in visited:
                    return parents[node]
                visited.add(parents[node])
                queue.append(parents[node])
        return None
        
        
    def build_reversed_graph(self, root) -> dict[TreeNode, TreeNode]:
        g = {}
        q = deque([(root, root)])
        while q:
            node, parent = q.popleft()
            g[node] = parent
            if node.left:
                q.append((node.left, node))
            if node.right:
                q.append((node.right, node))
        g.pop(root)
        return g