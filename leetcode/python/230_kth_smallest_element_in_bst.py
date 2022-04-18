class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        return self.helper(root, k)[1]

    def helper(self, root: TreeNode | None, k: int) -> tuple[bool, int]:
        if not root:
            return (False, k)
        
        l = self.helper(root.left, k)
        if l[0]:
            return l
        k = l[1] - 1
        if k == 0:
            return (True, root.val)
        r = self.helper(root.right, k)
        if r[0]:
            return r
        return (False, r[1])