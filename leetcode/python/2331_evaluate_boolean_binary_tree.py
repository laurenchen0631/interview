# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == 1

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:
            return left or right
        if root.val == 3:
            return left and right
        