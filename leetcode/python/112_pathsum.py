# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # if root == None:
        #     return False
        # return self._hasPathSumHelper2(root, targetSum)
        if root == None:
            return False

        targetSum -= root.val
        if root.left == None and root.right == None:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    def _hasPathSumHelper(self, node: TreeNode, remain: int) -> bool:
        remain = remain - node.val
             
        if node.left != None and self._hasPathSumHelper(node.left, remain):
            return True
        if node.right != None and self._hasPathSumHelper(node.right, remain):
            return True
        
        if node.left == None and node.right == None:
            return remain == 0