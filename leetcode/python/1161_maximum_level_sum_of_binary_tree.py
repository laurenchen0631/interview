# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        l = 1
        res = (1, root.val)
        q = [root]
        while q:
            tmp = []
            curSum = 0
            for node in q:
                curSum += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if curSum > res[1]:
                res = (l, curSum)
            q = tmp
            l += 1
        return res[0]