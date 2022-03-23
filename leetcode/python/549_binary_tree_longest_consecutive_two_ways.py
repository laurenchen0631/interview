class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.maximum: int = 0

    def longestConsecutive(self, root: TreeNode | None) -> int:
        self.dfs(root)
        return self.maximum
    
    def dfs(self, root: TreeNode | None) -> tuple[int, int]:
        if not root:
            return (0, 0)
        asc = desc = 1
        if root.left:
            left = self.dfs(root.left)
            if root.left.val == root.val - 1:
                desc = left[1] + 1
            elif root.left.val == root.val + 1:
                asc = left[0] + 1
        if root.right:
            right = self.dfs(root.right)
            if root.right.val == root.val - 1:
                desc = max(desc, right[1] + 1)
            elif root.right.val == root.val + 1:
                asc = max(asc, right[0] + 1)
        self.maximum = max(self.maximum, asc + desc - 1)
        return (asc, desc)
