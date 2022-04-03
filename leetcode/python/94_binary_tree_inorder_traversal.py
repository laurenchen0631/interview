# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        res: list[int] = []
        stack: list[TreeNode] = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res