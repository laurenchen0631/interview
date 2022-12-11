from math import inf
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        def getmax(root: TreeNode | None) -> tuple[int, int]:
            if not root:
                return (-sys.maxsize, -sys.maxsize)
            
            l = getmax(root.left)
            r = getmax(root.right)
            return (
                max(l[0], r[0], 0) + root.val,
                max(max(l), max(r), root.val + l[0] + r[0])
            )
        return max(getmax(root))