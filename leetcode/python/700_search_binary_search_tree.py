# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        node = root
        while node:
            if node.val == val:
                return node
            elif node.val < val:
                node = node.right
            else:
                node = node.left
        return None
        