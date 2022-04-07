# Definition for a binary tree node.
from calendar import c


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        nums = set[int]()
        stack: list[TreeNode | None] = [root]
        while stack:
            p = stack.pop()
            if not p:
                continue
            t = k - p.val
            if t in nums:
                return True
            nums.add(p.val)
            stack.append(p.left)
            stack.append(p.right)
        return False