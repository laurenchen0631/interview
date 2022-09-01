# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count: int = 0
        stack = [(root, root.val)]
        while stack:
            node, curMax = stack.pop()
            if curMax <= node.val:
                count += 1
                curMax = node.val
            if node.left:
                stack.append((node.left, curMax))
            if node.right:
                stack.append((node.right, curMax))
        return count
        