# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        
        def generate(i: int, j: int) -> list[TreeNode | None]:
            if i > j:
                return [None]
            res: list[TreeNode | None] = []
            for k in range(i, j + 1):
                left = generate(i, k - 1)
                right = generate(k + 1, j)
                for l in left:
                    for r in right:
                        res.append(TreeNode(k, l, r))
            return res
        
        res = generate(1, n)
        return res
