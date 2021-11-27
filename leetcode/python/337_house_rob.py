# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode | None) -> int:
        # return self._dfsHelper(root, False)
        return max(self._dfsOpt(root))

    @lru_cache(None)
    def _dfsHelper(self, node: TreeNode | None, isPrevRobbed: bool) -> int:
        if node == None:
            return 0

        current = 0 if isPrevRobbed else node.val + self._dfsHelper(node.left, True) + self._dfsHelper(node.right, True)
        next = self._dfsHelper(node.left, False) + self._dfsHelper(node.right, False)

        return max(current, next)


    def _dfsOpt(self, node: TreeNode | None) -> tuple[int, int]:
        if not node:
            return [0, 0]
        
        leftRes = self._dfsOpt(node.left)
        rightRes = self._dfsOpt(node.right)

        robbed = node.val + leftRes[1] + rightRes[1]
        skipped = max(leftRes) + max(rightRes)

        return [robbed, skipped]
