# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode | None) -> TreeNode | None:
        self.helper(root, 0)
        return root
    
    def helper(self, root: TreeNode | None, acc: int) -> int:
        if not root:
            return 0
        r = self.helper(root.right, acc)
        root.val += r + acc
        l = self.helper(root.left, root.val)
        return root.val + l - acc
        