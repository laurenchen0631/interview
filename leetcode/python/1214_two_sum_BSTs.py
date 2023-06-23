# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: TreeNode | None, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        
        # find target from two BST
        values = set()
        stack = [root1]
        cur = root1
        while stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            values.add(cur.val)
            cur = cur.right

        stack = [root2]
        while stack:
            node = stack.pop()
            if target - node.val in values:
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False