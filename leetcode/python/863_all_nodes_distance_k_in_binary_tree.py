# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        g = self.buildGraph(root)
        q = [target]
        visited = set[int]([target.val])
        while q:
            if k == 0:
                return [node.val for node in q]
            tmp = []
            for node in q:
                for neighbor in g[node.val]:
                    if neighbor.val not in visited:
                        visited.add(neighbor.val)
                        tmp.append(neighbor)
            q = tmp
            k -= 1
        return []
    
    def buildGraph(self, root: TreeNode) -> dict[int, list[TreeNode]]:
        g = dict[int, list[TreeNode]]()
        stack = [(root, root)]
        while stack:
            node, parent = stack.pop()
            g[node.val] = [parent]
            if node.left:
                stack.append((node.left, node))
                g[node.val].append(node.left)
            if node.right:
                stack.append((node.right, node))
                g[node.val].append(node.right)
        return g
        