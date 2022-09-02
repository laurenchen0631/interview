
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root:
            return []
        
        levels = []
        stack = [(root, 0)]
        while stack:
            node, l = stack.pop()
            if len(levels) == l:
                levels.append([0, 0])
            levels[l][0] += node.val
            levels[l][1] += 1
            if node.left:
                stack.append((node.left, l+1))
            if node.right:
                stack.append((node.right, l+1))
        return [n/k for n, k in levels]
            