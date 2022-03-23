# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.longest: int = 0

    def longestConsecutive(self, root: TreeNode | None) -> int:
        self.dfs(root)
        return self.longest

    def dfs(self, root: TreeNode | None):
        if not root:
            return 0
        
        longestLeft = self.dfs(root.left) + 1
        if root.left and root.left.val != root.val + 1:
            longestLeft = 1

        longestRight = self.dfs(root.right) + 1
        if root.right and root.right.val != root.val + 1:
            longestRight = 1

        self.longest = max(self.longest, longestLeft, longestRight)

        return max(longestLeft, longestRight)



        