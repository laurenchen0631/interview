# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        if not root:
            return 0
        
        return (
            (self.rangeSumBST(root.left, low, high) if root.val >= low else 0) +
            (self.rangeSumBST(root.right, low, high) if root.val <= high else 0) +
            (root.val if low <= root.val <= high else 0)
        )

        