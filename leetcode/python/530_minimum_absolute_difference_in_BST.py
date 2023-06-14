class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def traverse(node: TreeNode | None):
            if node is None:
                return []
            return traverse(node.left) + [node.val] + traverse(node.right)
        vals = traverse(root)
        res = vals[1] - vals[0]
        for i in range(2, len(vals)):
            res = min(res, vals[i] - vals[i-1])
        return res