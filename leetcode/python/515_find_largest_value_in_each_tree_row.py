
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        q = [root]
        res = []
        while q:
            cur_max = q[0].val
            tmp = []
            for node in q:
                cur_max = max(cur_max, node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(cur_max)
            q = tmp
        return res
                
        
        