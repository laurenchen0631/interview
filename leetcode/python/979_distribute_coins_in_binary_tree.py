# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res += abs(left) + abs(right)
        return root.val + left + right - 1
        