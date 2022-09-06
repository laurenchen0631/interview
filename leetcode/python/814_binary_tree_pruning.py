class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        def helper(root: TreeNode | None) -> bool:
            if root is None:
                return False
            l = helper(root.left)
            r = helper(root.right)
            if not l:
                root.left = None
            if not r:
                root.right = None
            return root.val == 1 or l or r
        return root if helper(root) else None
        