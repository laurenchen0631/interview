# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.helper(root)[0]
    
    def helper(self, root: TreeNode) -> tuple[TreeNode, TreeNode]:
        if not root.left and not root.right:
            return (root, root)
        
        l = self.helper(root.left) if root.left else None
        r = self.helper(root.right) if root.right else None
        root.left = None
        if l and r:
            l[1].right = root
            root.right = r[0]
            return (l[0], r[1])
        elif not l:
            root.right = r[0]
            return (root, r[1])
        else:
            l[1].right = root
            return (l[0], root)
