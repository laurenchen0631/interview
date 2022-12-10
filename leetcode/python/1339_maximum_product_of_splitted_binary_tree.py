# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: TreeNode | None) -> int:
        total = self.getTotal(root)
        res: int = 0
        def split(root: TreeNode | None) -> int:
            if not root:
                return 0
            nonlocal res
            l = split(root.left)
            r = split(root.right)
            if root.left:
                res = max(res, (total - l) * l)
            if root.right:
                res = max(res, (total - r) * l)
            return l + r + root.val
        
        split(root)
        return res % (10 ** 9 + 7)
        
    def getTotal(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        stack = [root]
        res = 0
        while stack:
            p = stack.pop()
            res += p.val
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        return res