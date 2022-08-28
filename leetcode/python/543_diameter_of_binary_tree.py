# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.cache: dict[TreeNode, int] = {}

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        return max(l+r, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    
    def getDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        if root in self.cache:
            return self.cache[root]
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        self.cache[root] = max(l, r) + 1
        return self.cache[root]