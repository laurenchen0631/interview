from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        res = deque[tuple[int, int]]([[]])
        stack = [(root, 0, 0)]
        leftmost = rightmost = 0
        while stack:
            node, r, c = stack.pop()
            if c < leftmost:
                res.appendleft([])
                leftmost = c
            elif c > rightmost:
                res.append([])
                rightmost = c
            res[c-leftmost].append((r, node.val))
            if node.left:
                stack.append((node.left, r+1, c-1))
            if node.right:
                stack.append((node.right, r+1, c+1))
        return [[v[1] for v in sorted(col)] for col in res]