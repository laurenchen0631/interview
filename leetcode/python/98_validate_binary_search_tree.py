# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.helper(root) != None

    def helper(self, root: TreeNode | None) -> tuple[int, int]:
        if not root:
            return None

        l = self.helper(root.left)
        r = self.helper(root.right)
        if l and r:
            return (l[0], r[1]) if l[1] < root.val < r[0] else None
        elif (not l and root.left) or (not r and root.right):
            return None
        elif l:
            return (l[0], root.val) if l[1] < root.val else None
        elif r:
            return (root.val, r[1]) if root.val < r[0] else None
        else:
            return (root.val, root.val)

    
    def _isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def validate(node: TreeNode, low: int, high: int) -> bool:
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root, -math.inf, math.inf)