from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        res: int = 0
        def dfs(root: TreeNode | None, path: int) -> None:
            if not root:
                return
            nonlocal res
            
            path += root.val
            res += prefix[path-targetSum]
            prefix[path] += 1
            dfs(root.left, path)
            dfs(root.right, path)
            prefix[path] -= 1
        dfs(root, 0)
        return res