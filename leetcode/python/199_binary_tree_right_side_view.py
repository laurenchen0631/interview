from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        
        queue = deque([root])
        res: list[int] = []

        while queue:
            tmp = deque()
            node: TreeNode | None = None
            while queue:
                node = queue.popleft()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(node.val)
            queue = tmp
        return res