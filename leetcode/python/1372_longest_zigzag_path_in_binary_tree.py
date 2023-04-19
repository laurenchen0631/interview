# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        res = 0
        def dfs(node: TreeNode | None, is_left: bool, visited: int) -> None:
            if not node:
                return
            
            nonlocal res
            res = max(res, visited - 1)
            if is_left:
                dfs(node.left, False, visited + 1)
                dfs(node.right, True, 2)
            else:
                dfs(node.left, False, 2)
                dfs(node.right, True, visited + 1)
            
        dfs(root, True, 1)
        dfs(root, False, 1)
        return res