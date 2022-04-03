# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> int | None:
        if not root:
            return []
        
        res: list[int] = []
        stack = [root, root]
        while stack:
            p = stack.pop()
            if stack and p == stack[-1]:
                if p.right:
                    stack.extend([p.right, p.right])
                if p.left:
                    stack.extend([p.left, p.left])
            else:
                res.append(p.val)
        return res