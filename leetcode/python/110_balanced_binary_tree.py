class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def helper(root: TreeNode | None) -> tuple[bool, int]:
            if not root:
                return (True, 0)
            
            left = helper(root.left)
            if not left[0]:
                return (False, 0)
            right = helper(root.right)
            if not right[0] or abs(left[1] - right[1]) > 1:
                return (False, 0)
            return (True, max(left[1], right[1]) + 1)
        return helper(root)[0]