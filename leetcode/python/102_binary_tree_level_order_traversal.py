# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q = deque([None, root])
        res: list[list[int]] = [[]]
        while q:
            node = q.pop()
            if not node:
                if q:
                    res.append([])
                    q.appendleft(None)
                continue
            res[-1].append(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        return res