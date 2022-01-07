# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root:
            return self.isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

    def isSame(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        
        return root.val == subRoot.val and self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
        