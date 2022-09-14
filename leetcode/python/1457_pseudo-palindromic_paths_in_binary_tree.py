# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode | None) -> int:
        if not root:
            return 0
        bucket = [0] * 10
        res: int = 0
        def dfs(root: TreeNode) -> None:
            bucket[root.val] += 1
            nonlocal res
            if not root.left and not root.right:
                res += self.isPseudoPalindrome(bucket)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            bucket[root.val] -= 1
        dfs(root)
        return res

    def isPseudoPalindrome(self, bucket: list[int]) -> bool:
        odds: int = 0
        for count in bucket:
            odds += count & 1
            if odds == 2:
                return False
        return True
        