# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            (node, l) = q.popleft()
            if node.left:
                q.append((node.left, l+1))
            if node.right:
                q.append((node.right, l+1))
            if not q:
                return l
