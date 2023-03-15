class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        res: int = 0
        def dfs(node: TreeNode | None, num: int) -> None:
            nonlocal res
            if node:
                num = num * 10 + node.val
                if not node.left and not node.right:
                    res += num
                else:
                    dfs(node.left, num)
                    dfs(node.right, num)
        dfs(root, 0)
        return res