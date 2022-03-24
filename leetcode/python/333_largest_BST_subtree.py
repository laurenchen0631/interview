# Definition for a binary tree node.
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.maximum: int = 0

    def largestBSTSubtree(self, root: TreeNode | None) -> int:
        self.searchBST(root)
        return self.maximum

    def searchBST(self, root: TreeNode | None) -> tuple[int, int, int]:
        if not root:
            return (0, inf, -inf)
        
        left = self.searchBST(root.left)
        right = self.searchBST(root.right)
        if left[0] > -1 and right[0] > -1 and root.val > left[2] and root.val < right[1]:
            n = left[0] + right[0] + 1
            self.maximum = max(self.maximum, n)
            return (n, min(left[1], root.val), max(right[2], root.val))
        return (-1, 0, 0)