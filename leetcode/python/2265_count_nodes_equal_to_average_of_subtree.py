# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        res = 0
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if not node:
                return (0, 0)
            l = dfs(node.left)
            r = dfs(node.right)
            total = node.val + l[0] + r[0]
            count = 1 + l[1] + r[1]
            avg = total // count
            if avg == node.val:
                nonlocal res
                res += 1
            return (total, count)
        dfs(root)
        return res
            
        