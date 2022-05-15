# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        q = deque([root, None])
        res = 0
        while q:
            p = q.popleft()
            if not p:
                if q:
                    q.append(None)
                    res = 0
                continue
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
            res += p.val
        return res